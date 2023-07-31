"use strict";(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[3535],{87814:function(e,t,i){i.d(t,{K:function(){return a}});var r=i(22951),n=i(91976),o=i(50641),a=function(){function e(){(0,r.Z)(this,e),this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}return(0,n.Z)(e,[{key:"manageFormClearListener",value:function(e,t,i){null!=this.formClearListener&&this.lastWidgetMgr===e&&this.lastFormId===t||(this.disconnect(),(0,o.bM)(t)&&(this.formClearListener=e.addFormClearedListener(t,i),this.lastWidgetMgr=e,this.lastFormId=t))}},{key:"disconnect",value:function(){var e;null===(e=this.formClearListener)||void 0===e||e.disconnect(),this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}}]),e}()},3535:function(e,t,i){i.r(t),i.d(t,{default:function(){return b}});var r=i(11026),n=i(22951),o=i(91976),a=i(67591),l=i(94337),s=i(66845),u=i(97142),d=i(87814),p=i(98478),m=i(86659),c=i(8879),h=i(68411),f=i(50641),g=i(40864),v=function(e){(0,a.Z)(i,e);var t=(0,l.Z)(i);function i(){var e;(0,n.Z)(this,i);for(var o=arguments.length,a=new Array(o),l=0;l<o;l++)a[l]=arguments[l];return(e=t.call.apply(t,[this].concat(a))).formClearHelper=new d.K,e.state={value:e.initialValue},e.commitWidgetValue=function(t){e.props.widgetMgr.setStringValue(e.props.element,e.state.value,t)},e.onFormCleared=function(){e.setState((function(e,t){return{value:t.element.default}}),(function(){return e.commitWidgetValue({fromUi:!0})}))},e.handleChange=function(t){var i;i=null===t?e.initialValue:e.dateToString(t),e.setState({value:i},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.stringToDate=function(e){var t=e.split(":").map(Number),i=(0,r.Z)(t,2),n=i[0],o=i[1],a=new Date;return a.setHours(n),a.setMinutes(o),a},e.dateToString=function(e){var t=e.getHours().toString().padStart(2,"0"),i=e.getMinutes().toString().padStart(2,"0");return"".concat(t,":").concat(i)},e}return(0,o.Z)(i,[{key:"initialValue",get:function(){var e=this.props.widgetMgr.getStringValue(this.props.element);return void 0!==e?e:this.props.element.default}},{key:"componentDidMount",value:function(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}},{key:"componentDidUpdate",value:function(){this.maybeUpdateFromProtobuf()}},{key:"componentWillUnmount",value:function(){this.formClearHelper.disconnect()}},{key:"maybeUpdateFromProtobuf",value:function(){this.props.element.setValue&&this.updateFromProtobuf()}},{key:"updateFromProtobuf",value:function(){var e=this,t=this.props.element.value;this.props.element.setValue=!1,this.setState({value:t},(function(){e.commitWidgetValue({fromUi:!1})}))}},{key:"render",value:function(){var e,t=this.props,i=t.disabled,r=t.width,n=t.element,o=t.widgetMgr,a={width:r},l={Select:{props:{disabled:i,overrides:{ControlContainer:{style:{borderLeftWidth:"1px",borderRightWidth:"1px",borderTopWidth:"1px",borderBottomWidth:"1px"}},IconsContainer:{style:function(){return{paddingRight:".5rem"}}},ValueContainer:{style:function(){return{paddingRight:".5rem",paddingLeft:".5rem",paddingBottom:".5rem",paddingTop:".5rem"}}},SingleValue:{props:{className:"stTimeInput-timeDisplay"}},Dropdown:{style:function(){return{paddingTop:0,paddingBottom:0}}},Popover:{props:{overrides:{Body:{style:function(){return{marginTop:"1px"}}}}}}}}}};return this.formClearHelper.manageFormClearListener(o,n.formId,this.onFormCleared),(0,g.jsxs)("div",{className:"stTimeInput",style:a,children:[(0,g.jsx)(p.O,{label:n.label,disabled:i,labelVisibility:(0,f.iF)(null===(e=n.labelVisibility)||void 0===e?void 0:e.value),children:n.help&&(0,g.jsx)(m.dT,{children:(0,g.jsx)(c.Z,{content:n.help,placement:h.u.TOP_RIGHT})})}),(0,g.jsx)(u.Z,{format:"24",step:n.step?Number(n.step):900,value:this.stringToDate(this.state.value),onChange:this.handleChange,overrides:l,creatable:!0,"aria-label":n.label})]})}}]),i}(s.PureComponent),b=v}}]);