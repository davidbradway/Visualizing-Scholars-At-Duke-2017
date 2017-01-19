/**
 * Adobe Edge: symbol definitions
 */
(function($, Edge, compId){
//images folder
var im='images/';

var fonts = {};


var resources = [
];
var symbols = {
"stage": {
   version: "2.0.0",
   minimumCompatibleVersion: "2.0.0",
   build: "2.0.0.250",
   baseState: "Base State",
   initialState: "Base State",
   gpuAccelerate: false,
   resizeInstances: false,
   content: {
         dom: [
         {
            id:'forms_transmission',
            display:'none',
            type:'image',
            rect:['228px','143px','75px','49px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"forms_transmission2.svg",'0px','0px']
         },
         {
            id:'forms_server_client',
            type:'image',
            rect:['0px','0px','730px','384px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"forms_server_client.svg",'0px','0px']
         },
         {
            id:'forms_browser',
            type:'image',
            rect:['0px','0px','730px','384px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"forms_browser.svg",'0px','0px']
         },
         {
            id:'forms_website',
            type:'image',
            rect:['0px','0px','730px','384px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"forms_website.svg",'0px','0px']
         },
         {
            id:'forms_searchform',
            type:'image',
            rect:['0px','0px','730px','384px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"forms_searchform.svg",'0px','0px']
         },
         {
            id:'forms_results',
            type:'image',
            rect:['0px','0px','730px','384px','auto','auto'],
            clip:['rect(0px 730pxpx 384pxpx 0px)'],
            fill:["rgba(0,0,0,0)",im+"forms_results.svg",'0px','0px']
         }],
         symbolInstances: [

         ]
      },
   states: {
      "Base State": {
         "${_forms_browser}": [
            ["style", "top", '0px'],
            ["style", "opacity", '0'],
            ["style", "left", '0px']
         ],
         "${_forms_transmission}": [
            ["style", "top", '143px'],
            ["style", "display", 'none'],
            ["style", "left", '228px'],
            ["transform", "rotateZ", '0deg']
         ],
         "${_forms_searchform}": [
            ["style", "top", '0px'],
            ["style", "opacity", '0'],
            ["style", "left", '0px']
         ],
         "${_Stage}": [
            ["color", "background-color", 'rgba(255,255,255,0.00)'],
            ["style", "width", '730px'],
            ["style", "height", '384px'],
            ["style", "overflow", 'visible']
         ],
         "${_forms_website}": [
            ["style", "top", '0px'],
            ["style", "opacity", '0'],
            ["style", "left", '0px']
         ],
         "${_forms_results}": [
            ["style", "top", '0px'],
            ["style", "opacity", '1'],
            ["style", "clip", [120,320,120,97], {valueTemplate:'rect(@@0@@px @@1@@px @@2@@px @@3@@px)'} ],
            ["style", "left", '0px']
         ],
         "${_forms_server_client}": [
            ["style", "top", '0px'],
            ["style", "opacity", '0'],
            ["style", "left", '0px']
         ]
      }
   },
   timelines: {
      "Default Timeline": {
         fromState: "Base State",
         toState: "",
         duration: 3000,
         autoPlay: true,
         labels: {
            "start": 49,
            "continue": 1549
         },
         timeline: [
            { id: "eid76", tween: [ "color", "${_Stage}", "background-color", 'rgba(255,255,255,0.00)', { animationColorSpace: 'RGB', valueTemplate: undefined, fromValue: 'rgba(255,255,255,0.00)'}], position: 828, duration: 0 },
            { id: "eid61", tween: [ "style", "${_forms_transmission}", "display", 'none', { fromValue: 'none'}], position: 49, duration: 0 },
            { id: "eid62", tween: [ "style", "${_forms_transmission}", "display", 'block', { fromValue: 'none'}], position: 1549, duration: 0 },
            { id: "eid63", tween: [ "style", "${_forms_transmission}", "display", 'none', { fromValue: 'block'}], position: 2436, duration: 0 },
            { id: "eid2", tween: [ "style", "${_Stage}", "width", '730px', { fromValue: '730px'}], position: 49, duration: 0 },
            { id: "eid52", tween: [ "style", "${_forms_transmission}", "left", '528px', { fromValue: '228px'}], position: 1549, duration: 331 },
            { id: "eid54", tween: [ "style", "${_forms_transmission}", "left", '225px', { fromValue: '539px'}], position: 2116, duration: 320 },
            { id: "eid3", tween: [ "style", "${_Stage}", "height", '384px', { fromValue: '384px'}], position: 49, duration: 0 },
            { id: "eid25", tween: [ "style", "${_forms_results}", "clip", [120,320,215,97], { valueTemplate: 'rect(@@0@@px @@1@@px @@2@@px @@3@@px)', fromValue: [120,320,120,97]}], position: 2372, duration: 500 },
            { id: "eid59", tween: [ "transform", "${_forms_transmission}", "rotateZ", '0deg', { fromValue: '0deg'}], position: 1549, duration: 0 },
            { id: "eid60", tween: [ "transform", "${_forms_transmission}", "rotateZ", '180deg', { fromValue: '0deg'}], position: 2116, duration: 0 },
            { id: "eid5", tween: [ "style", "${_forms_website}", "opacity", '1', { fromValue: '0'}], position: 549, duration: 250 },
            { id: "eid13", tween: [ "style", "${_forms_searchform}", "opacity", '1', { fromValue: '0'}], position: 1049, duration: 250 },
            { id: "eid7", tween: [ "style", "${_forms_server_client}", "opacity", '1', { fromValue: '0'}], position: 49, duration: 250 },
            { id: "eid11", tween: [ "style", "${_forms_browser}", "opacity", '1', { fromValue: '0'}], position: 299, duration: 250 }         ]
      }
   }
}
};


Edge.registerCompositionDefn(compId, symbols, fonts, resources);

/**
 * Adobe Edge DOM Ready Event Handler
 */
$(window).ready(function() {
     Edge.launchComposition(compId);
});
})(jQuery, AdobeEdge, "clientserver");
