<template>
<div class="login">
<el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px" class="demo-ruleForm">
  <el-form-item label="手机号" required prop="phone":rules="[
    {required:ture, message:'必须为11位可用手机号',trigger:'blur'}
    ]">
    <el-input type="phonenum" v-model="ruleForm2.phone" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="验证码" prop="checkcode">
    <el-input type="checkcode" v-model="ruleForm2.checkcode" autocomplete="off"></el-input>
    <el-button @click="sendMsg" type="primary" :disabled="isDisabled">{{buttonName}}</el-button>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="login">登陆</el-button>
  </el-form-item>
</el-form>
</div>
</template>





    <!-- 先引入 Vue -->
	<script src="https://unpkg.com/vue/dist/vue.js"></script>
	<!-- 引入组件库 -->
	<script src="https://unpkg.com/element-ui/lib/index.js"></script>
	<script>
		new Vue({
			el: '#app',
			data: {
				buttonName: "发送短信",
				isDisabled: false,
                time: 10,
                ruleForm2:{
                    phone:'',
                    checkcode:''
                }
			},
			methods: {
				sendMsg() {
					let me = this;
                    me.isDisabled = true;
                    var sms_data={
                        phone:this.ruleForm2.phone
                    }
                    this.$http.post('/sendsms',phone).then(response => {
                    response = response.body;
                    


					let interval = window.setInterval(function() {
						me.buttonName = '（' + me.time + '秒）后重新发送';
						--me.time;
						if(me.time < 0) {
							me.buttonName = "重新发送";
							me.time = 10;
							me.isDisabled = false;
							window.clearInterval(interval);
						}
					}, 1000);
 
                },
                
                login: function(){
                    var postdata={
                        phone:this.ruleForm2.phone,
                        checkcode:this.ruleForm2.checkcode
                    }
                }
 
			}
 
		})
	</script>