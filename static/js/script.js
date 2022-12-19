// Add the following code if you want the name of the file appear on select
$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
  });

  $(function () {
    var nua = navigator.userAgent
    var isAndroid = (nua.indexOf('Mozilla/5.0') > -1 && nua.indexOf('Android ') > -1 && nua.indexOf('AppleWebKit') > -1 && nua.indexOf('Chrome') === -1)
    if (isAndroid) {
      $('select.form-control').removeClass('form-control').css('width', '100%')
    }
  })
  /*------------------------*/
  let speakBtn, translate, speakerMenu, language;
  let allVoices, langtags;
  let voiceIndex = 0;
  
  function init(){
    speakBtn = qs("#speakBtn");
    translate = qs("#translate"); 
    speakerMenu = qs("#speakerMenu");
    language = qs("#language");
    langtags = getLanguageTags();
    speakBtn.addEventListener("click",talk,false);
    speakerMenu.addEventListener("change",selectSpeaker,false);
    if (window.speechSynthesis) {
      if (speechSynthesis.onvoiceschanged !== undefined) {
        //Chrome gets the voices asynchronously so this is needed
        speechSynthesis.onvoiceschanged = setUpVoices;
      }
      setUpVoices(); //for all the other browsers
    }else{
      speakBtn.disabled = true;
      speakerMenu.disabled = true;
      qs("#warning").style.display = "block";
    }
  }
  function setUpVoices(){
    allVoices = getAllVoices();
    createSpeakerMenu(allVoices);
  }
  function getAllVoices() {
    let voicesall = speechSynthesis.getVoices();
    let vuris = [];
    let voices = [];
    voicesall.forEach(function(obj,index){
      let uri = obj.voiceURI;
      if (!vuris.includes(uri)){
        vuris.push(uri);
        voices.push(obj);
      }
    });
    voices.forEach(function(obj,index){obj.id = index;});
    return voices;
  }
  function createSpeakerMenu(voices){
    let code = ``;
    voices.forEach(function(vobj,i){
      code += `<option value=${vobj.id}>`;
      code += `${vobj.name} (${vobj.lang})`;
      code += vobj.voiceURI.includes(".premium") ? ' (premium)' : ``;
      code += `</option>`;
    });
    speakerMenu.innerHTML = code;
    speakerMenu.selectedIndex = voiceIndex;
  }
  //code for when the user selects a speaker
  function selectSpeaker(){
    voiceIndex = speakerMenu.selectedIndex;
    let sval = Number(speakerMenu.value);
    let voice = allVoices[sval];
    let langcode = voice.lang.substring(0,2);
    let langcodeobj = searchObjects(langtags,"code",langcode);
    language.innerHTML = langcodeobj[0].name;
  }
  function talk(){
    let sval = Number(speakerMenu.value);
    let u = new SpeechSynthesisUtterance();
    u.voice = allVoices[sval];
    u.lang = u.voice.lang;
    u.text = translate.value;
    u.rate = 1.2;
    speechSynthesis.speak(u);
  }
  function getLanguageTags(){
    let langs = ["af-Afrikaans","sq-Albania","am-Amharic","ar-Arabic","hy-Armenian","az-Azerbaijani","eu-Basque","be-Belarusian","bn-Bengali","bs-Bosnian","bg-Bulgarian","my-Burmese","ca-Catalan","ceb-Cebuano","ny-Chichewa","zh-CN-Chinese (Simplified)","zh-TW-Chinese (Traditional)","co-Corsican","hr-Croatian","cs-Czech","da-Danish","nl-Dutch","en-English","eo-Esperanto","et-Estonian","tl-Filipino","fi-Finnish","fr-French","fy-Frisian","gl-Galician","ka-Georgian","de-German","el-Greek","gu-Gujarati","ht-Haitian Creole","ha-Hausa","haw-Hawaiian","iw-Hebrew","hi-Hindi","hmn-Hmong","hu-Hungarian","is-Icelandic","ig-Igbo","id-Indonesian","ga-Irish Gaelic","it-Italian","ja-Japanese","jw-Javanese","kn-Kannada","kk-Kazakh","km-Khmer","rw-Kinyarwanda","ko-Korean","ku-Kurdish (Kurmanji)","ky-Kyrgyz","lo-Lao","la-Latin","lv-Latvian","lt-Lithuanian","lb-Luxembourgish","mk-Macedonian","mg-Malagasy","ms-Malay", "ml-Malayalam","mt-Maltese","mi-Maori","mr-Marathi","mn-Mongolian","ne-Nepali","no-Norwegian","or-Odia (Oriya)","ps-Pashto","fa-Prsian","pl-Polish","pt-Portuguese","pa-Punjabi","ro-Romanian","ru-Russian","sm-Samoan","gd-Scots Gaelic","sr-Serbian","st-Sesotho","sn-Shona","sd-Sindhi","si-Sinhala","sk-Slovak","sl-Slovenian","so-Somali","es-Spanish","su-Sundanese","sw-Swahili","sv-Swedish","tg-Tajik","ta-Tamil","tt-Tatar","te-Telugu","th-Thai","tr-Turkish","tk-Turkmen","uk-Ukrainian","ur-Urdu","ug-Uyghur","uz-Uzbek", "vi-Vietnamese","cy-Welsh","xh-Xhosa","yi-Yiddish","yo-Yoruba","zu-Zulu"];
    let langobjects = [];
    for (let i=0;i<langs.length;i++){
      let langparts = langs[i].split("-");
      langobjects.push({"code":langparts[0],"name":langparts[1]});
    }
    return langobjects;
  }
  // Generic utility functions
  function searchObjects(array,prop,term,casesensitive = false){
    //searches an array of objects for a given term in a given property
    //returns only those objects that test positive
    let regex = new RegExp(term, casesensitive ? "" : "i");
    let newArrayOfObjects = array.filter(obj => regex.test(obj[prop]));
    return newArrayOfObjects;
  }
  function qs(selectorText){
    //saves lots of typing for those who eschew Jquery
    return document.querySelector(selectorText);
  }
  document.addEventListener('DOMContentLoaded', function (e) {
    try {init();} catch (error){
      console.log("Data didn't load", error);}
  });
   


