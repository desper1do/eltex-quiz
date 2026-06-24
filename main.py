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
:root{{--bg:#f5f5f5;--sf:#fff;--bd:#e0e0e0;--bd2:#ddd;--tx:#1a1a1a;--tx2:#666;--tx3:#888}}
[data-theme=dark]{{--bg:#111;--sf:#1e1e1e;--bd:#2a2a2a;--bd2:#333;--tx:#e8e8e8;--tx2:#999;--tx3:#666}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,sans-serif;background:var(--bg);color:var(--tx);padding:1rem}}
.wrap{{max-width:680px;margin:0 auto}}
h1{{font-size:20px;font-weight:500;margin-bottom:1rem}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:1rem}}
.stat{{background:var(--sf);border:1px solid var(--bd);border-radius:10px;padding:.75rem;text-align:center}}
.stat-n{{font-size:24px;font-weight:500}}
.stat-l{{font-size:12px;color:var(--tx2);margin-top:2px}}
.card{{background:var(--sf);border:1px solid var(--bd);border-radius:12px;padding:1.25rem;margin-bottom:1rem}}
.q-meta{{font-size:13px;color:var(--tx3);margin-bottom:.75rem;display:flex;justify-content:space-between}}
.q-text{{font-size:16px;font-weight:500;line-height:1.5;margin-bottom:1rem}}
.opt{{width:100%;text-align:left;padding:10px 14px;margin-bottom:8px;border:1px solid var(--bd2);border-radius:8px;background:var(--sf);color:var(--tx);font-size:14px;cursor:pointer;transition:.15s}}
.opt:hover:not(:disabled){{border-color:var(--tx3);background:var(--bg)}}
.opt.correct{{background:#e8f5e9;border-color:#4caf50;color:#2e7d32;font-weight:500}}
.opt.wrong{{background:#ffebee;border-color:#ef5350;color:#c62828}}
.opt.reveal{{background:#e8f5e9;border-color:#4caf50;color:#2e7d32}}
.opt.selected{{background:#e3f2fd;border-color:#1976d2;color:#0d47a1;font-weight:500}}
.q-hint{{font-size:13px;color:#1976d2;margin-bottom:.75rem;font-style:italic}}
.btn{{padding:9px 18px;border:1px solid var(--bd2);border-radius:8px;background:var(--sf);color:var(--tx);font-size:14px;cursor:pointer;transition:.15s}}
.btn:hover{{background:var(--bg)}}
.btn-main{{background:var(--tx);color:var(--sf);border-color:transparent}}
.btn-main:hover{{opacity:.85}}
.tbtn{{padding:7px 9px;border:1px solid var(--bd2);border-radius:8px;background:var(--sf);color:var(--tx);cursor:pointer;display:flex;align-items:center;transition:.15s}}
.tbtn:hover{{background:var(--bg)}}
.tabs{{display:flex;gap:4px;background:var(--sf);border:1px solid var(--bd);border-radius:10px;padding:4px;margin-bottom:1rem}}
.tab{{flex:1;padding:8px;border:none;border-radius:7px;background:transparent;color:var(--tx2);font-size:14px;font-weight:500;cursor:pointer;transition:.15s}}
.tab.active{{background:var(--tx);color:var(--sf)}}
.tab:hover:not(.active){{background:var(--bg)}}
.grade-badge{{display:inline-flex;align-items:center;justify-content:center;font-size:32px;font-weight:700;width:72px;height:72px;border-radius:50%;border:3px solid currentColor;margin-bottom:.5rem}}
.g5{{color:#2e7d32}}.g4{{color:#1565c0}}.g3{{color:#e65100}}.gf{{color:#c62828}}
.result-big{{text-align:center;padding:2rem 0}}
.result-big .score{{font-size:48px;font-weight:500}}
.review-title{{font-size:15px;font-weight:500;margin-bottom:.75rem}}
.review-item{{padding:.75rem 0;border-top:1px solid var(--bd)}}
.review-qnum{{font-size:12px;color:var(--tx3);margin-bottom:.25rem}}
.review-qtext{{font-size:14px;font-weight:500;line-height:1.45;margin-bottom:.5rem}}
.review-ans{{font-size:13px;padding:2px 0;display:flex;gap:6px;align-items:baseline;line-height:1.4}}
.review-ans.bad{{color:#c62828}}
.review-ans.good{{color:#2e7d32}}
.hidden{{display:none}}
</style>
<script>(function(){{var t=localStorage.getItem('eltex-theme');if(t)document.documentElement.dataset.theme=t;}})();</script>
</head>
<body>
<div class="wrap">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:1rem"><h1 style="margin:0;flex:1;cursor:pointer" onclick="goHome()">Тренажёр Элтекс</h1><a href="answers.html" style="font-size:15px;font-weight:500;color:var(--tx);text-decoration:none;border:1px solid var(--bd2);padding:6px 14px;border-radius:8px">Все вопросы →</a><button class="tbtn" id="themeBtn" onclick="toggleTheme()" title="Сменить тему"></button></div>
<div class="tabs">
  <button class="tab active" id="tabQuiz" onclick="switchMode('quiz')">Тренажёр</button>
  <button class="tab" id="tabExam" onclick="switchMode('exam')">Экзамен</button>
</div>
<div class="stats" id="statsPane">
  <div class="stat"><div class="stat-n" id="sTotal">{len(questions)}</div><div class="stat-l">Вопросов</div></div>
  <div class="stat"><div class="stat-n" id="sScore">—</div><div class="stat-l">Счёт</div></div>
  <div class="stat"><div class="stat-n" id="sPct">—</div><div class="stat-l">Процент</div></div>
</div>
<div class="card" id="startPane">
  <div style="text-align:center;padding:1.5rem 0">
    <p style="color:var(--tx2);margin-bottom:1rem">База: {len(questions)} вопросов</p>
    <button class="btn btn-main" onclick="startQuiz()">Начать тест</button>
  </div>
</div>
<div class="card hidden" id="examStartPane">
  <div style="text-align:center;padding:1.5rem 0">
    <p style="font-size:20px;font-weight:600;margin-bottom:.6rem">Экзамен</p>
    <p style="color:var(--tx2);font-size:14px;line-height:1.8;margin-bottom:1.25rem">50 случайных вопросов &nbsp;·&nbsp; 2 балла за вопрос &nbsp;·&nbsp; Итого 100 баллов<br><b>75+</b> — оценка <b>5</b> + сертификат &nbsp;&nbsp; <b>65–74</b> — оценка <b>4</b><br><b>50–64</b> — оценка <b>3</b> &nbsp;&nbsp; <b>&lt;50</b> — экзамен не сдан</p>
    <button class="btn btn-main" onclick="startExam()">Начать экзамен</button>
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
    <div style="color:var(--tx2);margin-top:.5rem" id="resSub"></div>
  </div>
  <div style="text-align:center;margin-top:1rem">
    <button class="btn btn-main" onclick="startQuiz()">Ещё раз</button>
  </div>
</div>
<div class="card hidden" id="wrongPane"></div>
<div class="card hidden" id="examResPane">
  <div class="result-big">
    <div id="examBadge" class="grade-badge"></div>
    <div class="score" id="examScore"></div>
    <div id="examLabel" style="font-size:18px;font-weight:500;margin-top:.4rem"></div>
    <div id="examCert" style="font-size:14px;margin-top:.25rem;color:var(--tx2)"></div>
  </div>
  <div style="display:flex;gap:8px;justify-content:center;margin-top:1.5rem">
    <button class="btn" onclick="retakeExam()">Пересдать</button>
    <button class="btn btn-main" onclick="switchMode('quiz')">В тренажёр</button>
  </div>
</div>
<div class="card hidden" id="examWrongPane"></div>
</div>
<script>
const ALL={q_json};
let q=[],cur=0,states=[],mode='quiz';
const EXAM_N=50;
function $(x){{return document.getElementById(x)}}
function calcScore(){{return states.filter(function(s){{return s&&s.answered&&s.correct}}).length}}
function calcAnswered(){{return states.filter(function(s){{return s&&s.answered}}).length}}
function updateStats(){{
  const sc=calcScore(),an=calcAnswered();
  $('qLive').textContent=sc+' / '+an;
  $('sScore').textContent=an>0?sc:'—';
  $('sPct').textContent=an>0?Math.round(sc/an*100)+'%':'—';
}}
function switchMode(m){{
  mode=m;
  $('tabQuiz').classList.toggle('active',m==='quiz');
  $('tabExam').classList.toggle('active',m==='exam');
  $('statsPane').classList.toggle('hidden',m==='exam');
  ['startPane','resPane','wrongPane','qPane','examStartPane','examResPane','examWrongPane'].forEach(function(id){{$(id).classList.add('hidden');}});
  if(m==='quiz')$('startPane').classList.remove('hidden');
  else $('examStartPane').classList.remove('hidden');
}}
function goHome(){{
  ['resPane','wrongPane','qPane','examResPane','examWrongPane'].forEach(function(id){{$(id).classList.add('hidden');}});
  if(mode==='quiz')$('startPane').classList.remove('hidden');
  else $('examStartPane').classList.remove('hidden');
}}
function startQuiz(){{
  q=[...ALL].sort(()=>Math.random()-.5);
  cur=0;
  states=new Array(q.length).fill(null);
  $('startPane').classList.add('hidden');
  $('resPane').classList.add('hidden');
  $('wrongPane').classList.add('hidden');
  $('qPane').classList.remove('hidden');
  $('sScore').textContent='—';$('sPct').textContent='—';
  showQ();
}}
function startExam(){{
  q=[...ALL].sort(()=>Math.random()-.5).slice(0,EXAM_N);
  cur=0;
  states=new Array(q.length).fill(null);
  $('examStartPane').classList.add('hidden');
  $('examResPane').classList.add('hidden');
  $('examWrongPane').classList.add('hidden');
  $('qPane').classList.remove('hidden');
  showQ();
}}
function retakeExam(){{
  $('examResPane').classList.add('hidden');
  $('examWrongPane').classList.add('hidden');
  startExam();
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
  if(cur>=q.length){{
    if(mode==='exam')showExamResults();
    else showResults();
  }}else showQ();
}}
function buildReview(wp){{
  const wrong=[];
  states.forEach(function(st,i){{if(st&&st.answered&&!st.correct)wrong.push({{i:i,st:st}});}});
  if(!wrong.length){{wp.classList.add('hidden');return;}}
  wp.classList.remove('hidden');
  let html='<div class="review-title">Разбор ошибок ('+wrong.length+')</div>';
  wrong.forEach(function(item){{
    html+='<div class="review-item">';
    html+='<div class="review-qnum">Вопрос '+(item.i+1)+'</div>';
    html+='<div class="review-qtext">'+q[item.i].question+'</div>';
    item.st.opts.forEach(function(o){{
      if(o.cssClass==='wrong'){{
        html+='<div class="review-ans bad"><svg width="12" height="12" viewBox="0 0 12 12" fill="none"><line x1="2" y1="2" x2="10" y2="10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><line x1="10" y1="2" x2="2" y2="10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>'+o.text+'</span></div>';
      }} else if(o.cssClass==='correct'||o.cssClass==='reveal'){{
        html+='<div class="review-ans good"><svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M1.5 6l3 3 6-6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span>'+o.text+'</span></div>';
      }}
    }});
    html+='</div>';
  }});
  wp.innerHTML=html;
}}
function showResults(){{
  $('qPane').classList.add('hidden');
  $('resPane').classList.remove('hidden');
  const sc=calcScore();
  const pct=Math.round(sc/q.length*100);
  $('resFinal').textContent=sc+' / '+q.length;
  $('resSub').textContent=pct>=80?'Отлично! Готов к экзамену':pct>=60?'Неплохо, есть что повторить':'Надо ещё поучить — '+pct+'%';
  buildReview($('wrongPane'));
}}
function showExamResults(){{
  $('qPane').classList.add('hidden');
  $('examResPane').classList.remove('hidden');
  const sc=calcScore();
  const pts=Math.round(sc/EXAM_N*100);
  let grade,cls,cert;
  if(pts>=75){{grade='5';cls='g5';cert=true;}}
  else if(pts>=65){{grade='4';cls='g4';cert=false;}}
  else if(pts>=50){{grade='3';cls='g3';cert=false;}}
  else{{grade='—';cls='gf';cert=false;}}
  const badge=$('examBadge');
  badge.textContent=grade;badge.className='grade-badge '+cls;
  $('examScore').textContent=pts+' / 100 баллов';
  const lbl=$('examLabel');
  lbl.textContent=grade!=='—'?'Оценка '+grade:'Экзамен не сдан';lbl.className=cls;
  const certEl=$('examCert');
  certEl.textContent=cert?'Сертификат выдаётся':'Без сертификата';
  certEl.style.color=cert?'#2e7d32':'';
  buildReview($('examWrongPane'));
}}
const MOON='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
const SUN='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
function updateThemeBtn(){{const d=document.documentElement;const b=$('themeBtn');if(b)b.innerHTML=d.dataset.theme==='dark'?SUN:MOON;}}
function toggleTheme(){{const d=document.documentElement;d.dataset.theme=d.dataset.theme==='dark'?'light':'dark';localStorage.setItem('eltex-theme',d.dataset.theme);updateThemeBtn();}}
updateThemeBtn();
</script>
</body>
</html>"""


SVG_CHECK = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0;margin-top:2px"><path d="M2 7l3.5 3.5L12 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SVG_SEARCH = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="6.5" cy="6.5" r="4.5" stroke="currentColor" stroke-width="1.5"/><line x1="10" y1="10" x2="14" y2="14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'


def build_answers_html(questions):
    items_html = ""
    for i, q in enumerate(questions):
        opts_html = ""
        for o in q["options"]:
            if o["isCorrect"]:
                opts_html += (
                    f'<div class="opt opt-correct">'
                    f'{SVG_CHECK}<span>{o["text"]}</span>'
                    f'</div>'
                )
            else:
                opts_html += f'<div class="opt opt-wrong">{o["text"]}</div>'
        items_html += (
            f'<div class="item" data-q="{i+1}">'
            f'<div class="qnum">{i+1}</div>'
            f'<div class="qtext">{q["question"]}</div>'
            f'{opts_html}'
            f'</div>'
        )
    total = len(questions)
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Все вопросы — Элтекс</title>
<style>
:root{{--bg:#f5f5f5;--sf:#fff;--bd:#e0e0e0;--bd2:#ddd;--tx:#1a1a1a;--tx2:#666;--tx3:#888;--tx4:#aaa}}
[data-theme=dark]{{--bg:#111;--sf:#1e1e1e;--bd:#2a2a2a;--bd2:#333;--tx:#e8e8e8;--tx2:#999;--tx3:#666;--tx4:#555}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,sans-serif;background:var(--bg);color:var(--tx);padding:1rem}}
.wrap{{max-width:720px;margin:0 auto}}
.topbar{{display:flex;align-items:center;gap:8px;margin-bottom:1rem}}
h1{{font-size:20px;font-weight:500;flex:1}}
a.back{{font-size:13px;color:var(--tx2);text-decoration:none;border:1px solid var(--bd2);padding:4px 10px;border-radius:6px}}
.tbtn{{padding:7px 9px;border:1px solid var(--bd2);border-radius:8px;background:var(--sf);color:var(--tx);cursor:pointer;display:flex;align-items:center;transition:.15s}}
.tbtn:hover{{background:var(--bg)}}
.search-wrap{{position:relative;margin-bottom:1rem}}
#searchInput{{width:100%;padding:10px 14px 10px 38px;border:1px solid var(--bd2);border-radius:10px;font-size:15px;background:var(--sf);color:var(--tx);outline:none}}
#searchInput:focus{{border-color:var(--tx3)}}
.search-icon{{position:absolute;left:11px;top:50%;transform:translateY(-50%);pointer-events:none;color:var(--tx3)}}
.counter{{font-size:13px;color:var(--tx3);margin-bottom:.75rem}}
.item{{background:var(--sf);border:1px solid var(--bd);border-radius:12px;padding:1rem 1.25rem;margin-bottom:.6rem}}
.item.hidden{{display:none}}
.qnum{{font-size:12px;color:var(--tx4);margin-bottom:.3rem}}
.qtext{{font-size:15px;font-weight:500;line-height:1.5;margin-bottom:.6rem}}
.opt{{font-size:14px;line-height:1.4;padding:4px 0;display:flex;gap:6px;align-items:flex-start}}
.opt-correct{{color:#4caf50;text-decoration:underline;text-decoration-color:#4caf50;text-underline-offset:2px;font-weight:500}}
.opt-wrong{{color:var(--tx3);padding-left:20px}}
</style>
<script>(function(){{var t=localStorage.getItem('eltex-theme');if(t)document.documentElement.dataset.theme=t;}})();</script>
</head>
<body>
<div class="wrap">
<div class="topbar">
  <h1>Все вопросы — Элтекс</h1>
  <a href="index.html" class="back">← Тренажёр</a>
  <button class="tbtn" id="themeBtn" onclick="toggleTheme()" title="Сменить тему"></button>
</div>
<div class="search-wrap">
  <span class="search-icon">{SVG_SEARCH}</span>
  <input id="searchInput" type="search" placeholder="Поиск по вопросу или ответу..." autocomplete="off" oninput="filter()">
</div>
<div class="counter" id="counter">{total} вопросов</div>
<div id="list">
{items_html}
</div>
</div>
<script>
const items=Array.from(document.querySelectorAll('.item'));
function filter(){{
  const q=document.getElementById('searchInput').value.toLowerCase().trim();
  let n=0;
  items.forEach(function(el){{
    const match=!q||el.textContent.toLowerCase().includes(q);
    el.classList.toggle('hidden',!match);
    if(match)n++;
  }});
  document.getElementById('counter').textContent=n+' вопросов';
}}
const MOON='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
const SUN='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
function updateThemeBtn(){{const d=document.documentElement;const b=document.getElementById('themeBtn');if(b)b.innerHTML=d.dataset.theme==='dark'?SUN:MOON;}}
function toggleTheme(){{const d=document.documentElement;d.dataset.theme=d.dataset.theme==='dark'?'light':'dark';localStorage.setItem('eltex-theme',d.dataset.theme);updateThemeBtn();}}
updateThemeBtn();
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
    Path("answers.html").write_text(build_answers_html(questions), encoding="utf-8")
    print(f"index.html + answers.html собраны: {len(questions)} вопросов")
