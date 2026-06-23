#!/usr/bin/env python3
from google import genai
from google.genai import types
import json, os, sys, time
from pathlib import Path

API_KEY = os.environ.get("GEMINI_API_KEY", "")

def process_image(client, img_path):
    with open(img_path, "rb") as f:
        img_bytes = f.read()
    ext = Path(img_path).suffix.lower().lstrip(".")
    mt = {"jpg":"image/jpeg","jpeg":"image/jpeg","png":"image/png"}.get(ext,"image/jpeg")
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            types.Part.from_bytes(data=img_bytes, mime_type=mt),
            types.Part.from_text(text='Russian quiz screenshot (Элтекс). Correct answer = filled radio button (dark circle). Return ONLY valid JSON, no markdown: {"question":"...","options":[{"text":"...","isCorrect":true},{"text":"...","isCorrect":false}]}')
        ]
    )
    raw = response.text.replace("```json","").replace("```","").strip()
    return json.loads(raw)

def build_html(questions):
    q_json = json.dumps(questions, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Тренажёр Элтекс</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,sans-serif;background:#f5f5f5;color:#1a1a1a;padding:1rem}}
.wrap{{max-width:680px;margin:0 auto}}
h1{{font-size:20px;font-weight:500;margin-bottom:1rem}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:1rem}}
.stat{{background:#fff;border:1px solid #e0e0e0;border-radius:10px;padding:.75rem;text-align:center}}
.stat-n{{font-size:24px;font-weight:500}}
.stat-l{{font-size:12px;color:#666;margin-top:2px}}
.card{{background:#fff;border:1px solid #e0e0e0;border-radius:12px;padding:1.25rem;margin-bottom:1rem}}
.q-meta{{font-size:13px;color:#888;margin-bottom:.75rem;display:flex;justify-content:space-between}}
.q-text{{font-size:16px;font-weight:500;line-height:1.5;margin-bottom:1rem}}
.opt{{width:100%;text-align:left;padding:10px 14px;margin-bottom:8px;border:1px solid #ddd;border-radius:8px;background:#fff;font-size:14px;cursor:pointer;transition:.15s}}
.opt:hover:not(:disabled){{border-color:#888;background:#f9f9f9}}
.opt.correct{{background:#e8f5e9;border-color:#4caf50;color:#2e7d32;font-weight:500}}
.opt.wrong{{background:#ffebee;border-color:#ef5350;color:#c62828}}
.opt.reveal{{background:#e8f5e9;border-color:#4caf50;color:#2e7d32}}
.opt.selected{{background:#e3f2fd;border-color:#1976d2;color:#0d47a1;font-weight:500}}
.q-hint{{font-size:13px;color:#1976d2;margin-bottom:.75rem;font-style:italic}}
.btn{{padding:9px 18px;border:1px solid #ddd;border-radius:8px;background:#fff;font-size:14px;cursor:pointer}}
.btn:hover{{background:#f5f5f5}}
.btn-main{{background:#1a1a1a;color:#fff;border-color:transparent}}
.btn-main:hover{{opacity:.85}}
.result-big{{text-align:center;padding:2rem 0}}
.result-big .score{{font-size:48px;font-weight:500}}
.hidden{{display:none}}
</style>
</head>
<body>
<div class="wrap">
<h1>Тренажёр Элтекс</h1>
<div class="stats">
  <div class="stat"><div class="stat-n" id="sTotal">{len(questions)}</div><div class="stat-l">Вопросов</div></div>
  <div class="stat"><div class="stat-n" id="sScore">—</div><div class="stat-l">Счёт</div></div>
  <div class="stat"><div class="stat-n" id="sPct">—</div><div class="stat-l">Процент</div></div>
</div>
<div class="card" id="startPane">
  <div style="text-align:center;padding:1.5rem 0">
    <p style="color:#666;margin-bottom:1rem">База: {len(questions)} вопросов</p>
    <button class="btn btn-main" onclick="startQuiz()">Начать тест</button>
  </div>
</div>
<div class="card hidden" id="qPane">
  <div class="q-meta"><span id="qNum"></span><span id="qLive"></span></div>
  <div class="q-text" id="qText"></div>
  <div class="q-hint hidden" id="qHint"></div>
  <div id="qOpts"></div>
  <div class="hidden" id="checkRow" style="margin-top:.75rem">
    <button class="btn btn-main" onclick="checkMulti()">Проверить ответ</button>
  </div>
  <div class="hidden" id="nextRow" style="margin-top:.75rem">
    <button class="btn btn-main" onclick="nextQ()">Следующий</button>
  </div>
</div>
<div class="card hidden" id="resPane">
  <div class="result-big">
    <div class="score" id="resFinal"></div>
    <div style="color:#666;margin-top:.5rem" id="resSub"></div>
  </div>
  <div style="text-align:center;margin-top:1rem">
    <button class="btn btn-main" onclick="startQuiz()">Ещё раз</button>
  </div>
</div>
</div>
<script>
const ALL={q_json};
let q=[],cur=0,score=0,answered=0;
function $(x){{return document.getElementById(x)}}
function startQuiz(){{
  q=[...ALL].sort(()=>Math.random()-.5);
  cur=0;score=0;answered=0;
  $('startPane').classList.add('hidden');
  $('resPane').classList.add('hidden');
  $('qPane').classList.remove('hidden');
  showQ();
}}
function showQ(){{
  const item=q[cur];
  $('qNum').textContent='Вопрос '+(cur+1)+' из '+q.length;
  $('qLive').textContent=score+' / '+answered;
  $('qText').textContent=item.question;
  const opts=[...item.options].sort(()=>Math.random()-.5);
  const correctCount=opts.filter(function(o){{return o.isCorrect}}).length;
  const isMulti=correctCount>1;
  const hint=$('qHint');
  if(isMulti){{hint.textContent='Выберите '+correctCount+' '+(correctCount===2?'варианта':'вариантов');hint.classList.remove('hidden');}}
  else{{hint.classList.add('hidden');}}
  $('qOpts').innerHTML='';
  opts.forEach(function(o){{
    const b=document.createElement('button');
    b.className='opt';b.textContent=o.text;
    b.dataset.correct=o.isCorrect?'1':'0';
    b.dataset.selected='0';
    if(isMulti){{
      b.onclick=function(){{toggleOpt(b)}};
    }}else{{
      b.onclick=function(){{pick(b,o.isCorrect,opts)}};
    }}
    $('qOpts').appendChild(b);
  }});
  $('checkRow').classList.toggle('hidden',!isMulti);
  $('nextRow').classList.add('hidden');
}}
function toggleOpt(btn){{
  if(btn.disabled)return;
  if(btn.dataset.selected==='1'){{
    btn.dataset.selected='0';
    btn.classList.remove('selected');
  }}else{{
    btn.dataset.selected='1';
    btn.classList.add('selected');
  }}
}}
function checkMulti(){{
  const btns=Array.from(document.querySelectorAll('.opt'));
  btns.forEach(function(b){{b.disabled=true;b.classList.remove('selected');}});
  answered++;
  let allCorrect=true;
  btns.forEach(function(b){{
    const c=b.dataset.correct==='1';
    const s=b.dataset.selected==='1';
    if(c&&s){{b.classList.add('correct');}}
    else if(!c&&s){{b.classList.add('wrong');allCorrect=false;}}
    else if(c&&!s){{b.classList.add('reveal');allCorrect=false;}}
  }});
  if(allCorrect)score++;
  $('qLive').textContent=score+' / '+answered;
  $('sScore').textContent=score;
  $('sPct').textContent=Math.round(score/answered*100)+'%';
  $('checkRow').classList.add('hidden');
  $('nextRow').classList.remove('hidden');
}}
function pick(btn,correct,opts){{
  const btns=document.querySelectorAll('.opt');
  btns.forEach(function(b){{b.disabled=true}});
  answered++;
  if(correct){{btn.classList.add('correct');score++;}}
  else{{
    btn.classList.add('wrong');
    btns.forEach(function(b,i){{if(opts[i]&&opts[i].isCorrect)b.classList.add('reveal')}});
  }}
  $('qLive').textContent=score+' / '+answered;
  $('sScore').textContent=score;
  $('sPct').textContent=Math.round(score/answered*100)+'%';
  $('nextRow').classList.remove('hidden');
}}
function nextQ(){{
  cur++;
  if(cur>=q.length)showResults();
  else showQ();
}}
function showResults(){{
  $('qPane').classList.add('hidden');
  $('resPane').classList.remove('hidden');
  const pct=Math.round(score/q.length*100);
  $('resFinal').textContent=score+' / '+q.length;
  $('resSub').textContent=pct>=80?'Отлично! Готов к экзамену':pct>=60?'Неплохо, есть что повторить':'Надо ещё поучить — '+pct+'%';
}}
</script>
</body>
</html>"""

def main():
    if not API_KEY:
        print("Нет ключа! Запусти сначала:")
        print("  export GEMINI_API_KEY=ВАШ_КЛЮЧ")
        sys.exit(1)

    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    images = sorted(
        list(folder.glob("*.png")) +
        list(folder.glob("*.jpg")) +
        list(folder.glob("*.jpeg"))
    )

    if not images:
        print(f"Нет изображений в папке: {folder.absolute()}")
        sys.exit(1)

    out = Path("questions.json")
    questions = json.loads(out.read_text(encoding="utf-8")) if out.exists() else []
    done = {q.get("source","") for q in questions}
    remaining = [img for img in images if img.name not in done]

    print(f"Папка:      {folder.absolute()}")
    print(f"Всего фото: {len(images)}")
    print(f"Готово:     {len(done)}")
    print(f"Осталось:   {len(remaining)}\n")

    if not remaining:
        print("Все фото уже обработаны!")
    else:
        client = genai.Client(api_key=API_KEY)

        for i, img in enumerate(remaining):
            print(f"[{i+1}/{len(remaining)}] {img.name} ... ", end="", flush=True)
            try:
                parsed = process_image(client, img)
                q_text = parsed.get("question","")
                opts = parsed.get("options",[])
                if q_text and len(opts) >= 2 and any(o.get("isCorrect") for o in opts):
                    parsed["source"] = img.name
                    questions.append(parsed)
                    print(f"OK  {q_text[:55]}...")
                else:
                    print("нет правильного ответа")
            except Exception as e:
                print(f"ошибка: {str(e)[:70]}")

            out.write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")
            time.sleep(1.5)

    html_path = Path("quiz.html")
    html_path.write_text(build_html(questions), encoding="utf-8")
    print(f"\nСохранено {len(questions)} вопросов -> questions.json")
    print(f"Открой в браузере -> quiz.html")

if __name__ == "__main__":
    main()