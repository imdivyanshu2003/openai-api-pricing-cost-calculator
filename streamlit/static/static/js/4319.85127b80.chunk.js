"use strict";(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[4319],{87814:function(e,t,i){i.d(t,{K:function(){return a}});var n=i(22951),r=i(91976),o=i(50641),a=function(){function e(){(0,n.Z)(this,e),this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}return(0,r.Z)(e,[{key:"manageFormClearListener",value:function(e,t,i){null!=this.formClearListener&&this.lastWidgetMgr===e&&this.lastFormId===t||(this.disconnect(),(0,o.bM)(t)&&(this.formClearListener=e.addFormClearedListener(t,i),this.lastWidgetMgr=e,this.lastFormId=t))}},{key:"disconnect",value:function(){var e;null===(e=this.formClearListener)||void 0===e||e.disconnect(),this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}}]),e}()},94319:function(e,t,i){i.r(t),i.d(t,{default:function(){return h}});var n=i(22951),r=i(91976),o=i(67591),a=i(94337),l=i(66845),s=i(87814),u=i(97965),d=i(50641),m=i(40864),p=function(e){(0,o.Z)(i,e);var t=(0,a.Z)(i);function i(){var e;(0,n.Z)(this,i);for(var r=arguments.length,o=new Array(r),a=0;a<r;a++)o[a]=arguments[a];return(e=t.call.apply(t,[this].concat(o))).formClearHelper=new s.K,e.state={value:e.initialValue},e.commitWidgetValue=function(t){e.props.widgetMgr.setIntValue(e.props.element,e.state.value,t)},e.onFormCleared=function(){e.setState((function(e,t){return{value:t.element.default}}),(function(){return e.commitWidgetValue({fromUi:!0})}))},e.onChange=function(t){e.setState({value:t},(function(){return e.commitWidgetValue({fromUi:!0})}))},e}return(0,r.Z)(i,[{key:"initialValue",get:function(){var e=this.props.widgetMgr.getIntValue(this.props.element);return void 0!==e?e:this.props.element.default}},{key:"componentDidMount",value:function(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}},{key:"componentDidUpdate",value:function(){this.maybeUpdateFromProtobuf()}},{key:"componentWillUnmount",value:function(){this.formClearHelper.disconnect()}},{key:"maybeUpdateFromProtobuf",value:function(){this.props.element.setValue&&this.updateFromProtobuf()}},{key:"updateFromProtobuf",value:function(){var e=this,t=this.props.element.value;this.props.element.setValue=!1,this.setState({value:t},(function(){e.commitWidgetValue({fromUi:!1})}))}},{key:"render",value:function(){var e=this.props.element,t=e.options,i=e.help,n=e.label,r=e.labelVisibility,o=e.formId,a=e.placeholder,l=this.props,s=l.disabled,p=l.widgetMgr;return this.formClearHelper.manageFormClearListener(p,o,this.onFormCleared),(0,m.jsx)(u.Z,{label:n,labelVisibility:(0,d.iF)(null===r||void 0===r?void 0:r.value),options:t,disabled:s,width:this.props.width,onChange:this.onChange,value:this.state.value,help:i,placeholder:a})}}]),i}(l.PureComponent),h=p}}]);