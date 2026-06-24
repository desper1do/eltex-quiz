#!/usr/bin/env python3
import json
from pathlib import Path


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
  <div id="navRow" style="margin-top:.75rem;display:flex;gap:8px;align-items:center">
    <button class="btn" id="prevBtn" onclick="prevQ()">← Назад</button>
    <div style="flex:1"></div>
    <button class="btn btn-main hidden" id="checkBtn" onclick="checkMulti()">Проверить ответ</button>
    <button class="btn btn-main hidden" id="nextBtn" onclick="nextQ()">Следующий →</button>
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
let q=[],cur=0,states=[];
function $(x){{return document.getElementById(x)}}
function calcScore(){{return states.filter(function(s){{return s&&s.answered&&s.correct}}).length}}
function calcAnswered(){{return states.filter(function(s){{return s&&s.answered}}).length}}
function updateStats(){{
  const sc=calcScore(),an=calcAnswered();
  $('qLive').textContent=sc+' / '+an;
  $('sScore').textContent=an>0?sc:'—';
  $('sPct').textContent=an>0?Math.round(sc/an*100)+'%':'—';
}}
function startQuiz(){{
  q=[...ALL].sort(()=>Math.random()-.5);
  cur=0;
  states=new Array(q.length).fill(null);
  $('startPane').classList.add('hidden');
  $('resPane').classList.add('hidden');
  $('qPane').classList.remove('hidden');
  $('sScore').textContent='—';$('sPct').textContent='—';
  showQ();
}}
function showQ(){{
  const item=q[cur];
  $('qNum').textContent='Вопрос '+(cur+1)+' из '+q.length;
  updateStats();
  $('qText').textContent=item.question;
  if(!states[cur]){{
    states[cur]={{
      opts:[...item.options].sort(()=>Math.random()-.5).map(function(o){{
        return {{text:o.text,isCorrect:o.isCorrect,cssClass:'',disabled:false,selected:false}};
      }}),
      answered:false,correct:false
    }};
  }}
  const st=states[cur];
  const opts=st.opts;
  const correctCount=opts.filter(function(o){{return o.isCorrect}}).length;
  const isMulti=correctCount>1;
  const hint=$('qHint');
  if(isMulti){{hint.textContent='Выберите '+correctCount+' '+(correctCount===2?'варианта':'вариантов');hint.classList.remove('hidden');}}
  else{{hint.classList.add('hidden');}}
  $('qOpts').innerHTML='';
  opts.forEach(function(o,i){{
    const b=document.createElement('button');
    b.className='opt'+(o.cssClass?' '+o.cssClass:'')+(o.selected?' selected':'');
    b.textContent=o.text;
    b.dataset.correct=o.isCorrect?'1':'0';
    b.disabled=o.disabled;
    if(!o.disabled){{
      if(isMulti){{b.onclick=function(){{toggleOpt(b,i)}};}}
      else{{b.onclick=function(){{pick(b,o.isCorrect,i)}};}}
    }}
    $('qOpts').appendChild(b);
  }});
  $('checkBtn').classList.toggle('hidden',!isMulti||st.answered);
  $('nextBtn').classList.toggle('hidden',!st.answered);
  $('prevBtn').classList.toggle('hidden',cur===0);
}}
function toggleOpt(btn,i){{
  if(btn.disabled)return;
  const o=states[cur].opts[i];
  o.selected=!o.selected;
  if(o.selected){{btn.classList.add('selected');}}
  else{{btn.classList.remove('selected');}}
}}
function checkMulti(){{
  const st=states[cur];
  const opts=st.opts;
  let allCorrect=true;
  opts.forEach(function(o){{
    o.disabled=true;
    if(o.isCorrect&&o.selected){{o.cssClass='correct';}}
    else if(!o.isCorrect&&o.selected){{o.cssClass='wrong';allCorrect=false;}}
    else if(o.isCorrect&&!o.selected){{o.cssClass='reveal';allCorrect=false;}}
    o.selected=false;
  }});
  st.answered=true;st.correct=allCorrect;
  updateStats();
  Array.from($('qOpts').children).forEach(function(b,i){{
    const o=opts[i];
    b.className='opt'+(o.cssClass?' '+o.cssClass:'');
    b.disabled=true;
  }});
  $('checkBtn').classList.add('hidden');
  $('nextBtn').classList.remove('hidden');
}}
function pick(btn,isCorrect,i){{
  const st=states[cur];
  const opts=st.opts;
  opts.forEach(function(o){{o.disabled=true;}});
  st.answered=true;
  if(isCorrect){{opts[i].cssClass='correct';st.correct=true;}}
  else{{opts[i].cssClass='wrong';st.correct=false;opts.forEach(function(o){{if(o.isCorrect)o.cssClass='reveal';}});}}
  updateStats();
  Array.from($('qOpts').children).forEach(function(b,j){{
    const o=opts[j];b.className='opt'+(o.cssClass?' '+o.cssClass:'');b.disabled=true;
  }});
  $('nextBtn').classList.remove('hidden');
}}
function prevQ(){{if(cur>0){{cur--;showQ();}}}}
function nextQ(){{
  cur++;
  if(cur>=q.length)showResults();
  else showQ();
}}
function showResults(){{
  $('qPane').classList.add('hidden');
  $('resPane').classList.remove('hidden');
  const sc=calcScore();
  const pct=Math.round(sc/q.length*100);
  $('resFinal').textContent=sc+' / '+q.length;
  $('resSub').textContent=pct>=80?'Отлично! Готов к экзамену':pct>=60?'Неплохо, есть что повторить':'Надо ещё поучить — '+pct+'%';
}}
</script>
</body>
</html>"""


if __name__ == "__main__":
    questions = json.loads(Path("questions.json").read_text(encoding="utf-8"))
    draft_path = Path("questions_draft.json")
    if draft_path.exists():
        draft = json.loads(draft_path.read_text(encoding="utf-8"))
        questions = questions + draft
        print(f"  questions.json: {len(questions) - len(draft)} | questions_draft.json: {len(draft)}")
    Path("index.html").write_text(build_html(questions), encoding="utf-8")
    print(f"index.html собран: {len(questions)} вопросов")
