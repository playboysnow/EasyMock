<template>  
<div class="all"> 
  <el-container style="height:100%; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
  </el-aside>
   <el-container>
    <el-header style="text-align: right; font-size: 12px">
       <div class="icon_bar">
        <p>EasyMock</p> 
    </div>
    </el-header>

     <el-main>
  <div class="configArea">
  
  <el-form inline=true  ref="form" :model="form" >
    <div class="selectDiv">
  <el-form-item label="接口URL">
    <el-input v-model="form.url" placeholder="类似于/login" ></el-input>
  </el-form-item>
    </div>
  <div class="selectDiv">
  <el-form-item label="PORT">
    <el-input v-model="form.port" placeholder="保证要使用端口未被占用"></el-input>
  </el-form-item>
  </div>
  <div class="selectDiv">
  <el-form-item label="延时">
    <el-input v-model="form.sleeptime" placeholder="单位ms，输入1000 即1秒"></el-input>
  </el-form-item>
  </div>
 <div class="selectDiv">
  <el-form-item label="method方法">
    <el-select v-model="form.method"  multiple placeholder="可多选">
      <!--多选-->
      
      <el-option label="POST" value="POST"></el-option>
      <el-option label="GET" value="GET"></el-option>
      <el-option label="PUT" value="PUT"></el-option>
      <el-option label="HEAD" value="HEAD"></el-option>
    </el-select>
  </el-form-item>
 </div>
 <div class="selectDiv">
  <el-form-item label="类型">
    <el-select v-model="form.type"   placeholder="选择一种，必选">
      <el-option label="类型一" value="1"></el-option>
      <el-option label="类型二" value="2"></el-option>
      <el-option label="类型三" value="3"></el-option>
      <el-option label="类型四" value="4"></el-option>
    </el-select>
  </el-form-item>
  </div>
  <div class="selectDiv">
  <el-popover
    placement="top-start"
    title="示例"
    width="270"
    trigger="hover"
    content="类型一：接口地址http:XXX.xx.xx:port/url
             类型二：接口地址http:xxx.xx.xx:port/url/xx
             类型三:在类型一的基础上支持逻辑判断，
             根据判断逻辑返回不同的响应，需要修改server.py文件
             类型四:在类型二的基础上支持逻辑判断。        
    ">
    <el-button slot="reference">类型示例</el-button>
  </el-popover>
  </div>
  <div class="selectDiv">
  <el-form-item label="响应一">
    <el-input type="textarea" style="width:300px" :autosize="{ minRows: 4, maxRows: 8}" v-model="form.response" placeholder="类型一类型二 只使用响应一"></el-input>
  </el-form-item>
  </div>
  <div class="selectDiv">
   <el-form-item label="响应二">
    <el-input type="textarea"  style="width:300px" :autosize="{ minRows: 4, maxRows: 8}" v-model="form.response_fail" placeholder="类型三类型四时，需填写响应一响应二"></el-input>
  </el-form-item>
  </div>

   <div class="selectDiv">
  <el-form-item>
    <el-button type="primary" @click="add">生成配置</el-button>
    <el-button @click="clear">重置</el-button>
  </el-form-item>
 </div>
 </el-form>
</div>

<div class="tablelist">

<el-table :data="tableData" @row-click="get_row_info">
    <el-table-column prop="url" label="接口URL" >
      <!-- <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px">{{ scope.row.date }}</span>
      </template> -->
    </el-table-column>
    <el-table-column prop="method" label="请求方式" >
      </el-table-column>
    <el-table-column prop="desc" label="描述" >
      <!-- <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>URL: {{ scope.row.name }}</p>
          <p>response: {{ scope.row.address }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.name }}</el-tag>
          </div>
        </el-popover>
      </template> -->
    </el-table-column>
    <el-table-column prop="status" label="状态">
      <template  slot-scope="scope">
        <el-switch
  style="display: block"
  v-model="server_start"
  active-color="#13ce66"
  inactive-color="#ff4949"
  active-text="启动"
  inactive-text="停止"
  @change="start">
      </el-switch>
      </template>  
      </el-table-column>
    <el-table-column prop="modify" label="操作">
      <template slot-scope="scope">
        <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>  
    </el-table-column>
  </el-table>
  </div>
  </el-main>
  </el-container>
  

</el-container>
</div>
</template>











<script>
/*
todo:
1、CSS格式
2、数据传递
3、数据格式校验
4、json格式校验
5、手机号验证登陆
 */

  export default {
    
    name: 'mock',
    data() {

      return {
        form: {
          url: '',
          port: '',
          sleeptime: '',
          method:[],
          type:'',
          response:'',
          response_fail:''
        },
       table:[],
       server_start:false,
       F_table:[]
      }
    },
    computed: {
      tableData: function(){
        
        for (var val of this.table){
          console.log(val)
          //  val.url='ip地址'+':'+this.form.port+this.form.port
          val.url='http://xxx.xx.xx.xx:'+val.port+val.url
          
           val.desc='根据机器实际ip地址进行访问使用；'+val.url+'响应格式：'+val.response_succ
          
        /*
          if (val.type === 1 || 3){
            tb.url='http://'+'ip'+':'+this.port+this.url
          tb.desc=""
          }
          else if (val.type===2 ||4){
          tb.url='http://'+'ip'+':'+this.port+this.url+'/XXX'
          tb.desc=""
          }
        */  
        }

      return this.table
      }
    },
    methods: {
      get_row_info(row,event,column){
        console.log(row.url)
      },
      start: function(){
        if (this.server_start===true){
          this.$http.post('/mockstart',this.tableData[index].postdata)
        }
      },
      add: function(){
        /*this.table.append()*/
          var data={
            url:this.form.url,
          port:this.form.port,
          sleeptime:this.form.sleeptime,
          method:this.form.method,
          type:this.form.type,
          response:this.form.response,
          response_fail:this.form.response_fail
          }
          console.log(data)
          this.F_table.push(data)
          console.log(this.F_table)
          this.table=this.F_table
          // this.$alert("启动成功",'提示', {
          // confirmButtonText: '确定', 
          // })
        //  this.$http.post('/api/mockstart',this.form).then(response => {
        //   response = response.body;
          
        //   if (response.code==0){
        //     this.$alert("服务关闭",'提示', {
        //   confirmButtonText: '确定', 
        //     })
        //   }
        
        
         /* this.$alert(this.form,'提示', {
          confirmButtonText: '确定',  
          callback: action => {
              this.form={
          url: '',
          port: '',
          sleeptime: '',
          method:[],
          type:'',
          response:'',
          response_fail:''
        };
          }     
        });*/
         //})
      },
        
      
      mockstart: function(){

      },
     
       clear: function() {
        this.form={
          url: '',
          port: '',
          sleeptime: '',
          method:'',
          type:'',
          response_succ:'',
          response_fail:''
        };
      },
     /*手机号为数字 */
       checknum: function(callback){
        this.formInline.remobile=this.formInline.remobile.replace(/[^\.\d]/g,'');
        this.formInline.remobile=this.formInline.remobile.replace('.','');
        this.formInline.sendmobile=this.formInline.sendmobile.replace(/[^\.\d]/g,'');
        this.formInline.sendmobile=this.formInline.sendmobile.replace('.','');
         },
      /*下拉框监听 */
      change: function(callback) {
          if(this.formInline.region=="说吧"){
            
            this.$alert("说吧功能开发中", '提示', {
          confirmButtonText: '确定',
          callback: action => {
               this.formInline.region=="";
          },
          
        });
          
          }
      },
      onSubmit: function(callback) { 
        var isable=this.isable;
        var region=this.formInline.region;
        var remobile=this.formInline.remobile;
        var sendmobile=this.formInline.sendmobile;
        var textarea=this.textarea;
        /* 参数判断 */
         if(region=="说吧"){
            
            this.$alert("说吧功能开发中", '提示', {
          confirmButtonText: '确定',
          callback: action => {
               this.formInline.region=="";
          },
          
        });
          
          }
          else if (region=="") {
            this.$alert("类型不能为空", '提示', {
          confirmButtonText: '确定',        
        });
          }
          if (remobile=="") {
            this.$alert("收信人手机号不能为空", '提示', {
          confirmButtonText: '确定',        
        });
          }
          else if (remobile.length!=11){
            this.$alert("收信人手机号为11位数字", '提示', {
          confirmButtonText: '确定',        
        });
          }
        else if (sendmobile!=""&&sendmobile.length!=11){
            this.$alert("本人手机号为11位数字", '提示', {
          confirmButtonText: '确定',        
        });
          }
        var postdata = {
          "textarea":textarea,
          "remobile":remobile,
          "sendmobile":sendmobile,
          "region":region
        };
        /*调试参数
        this.$alert(postdata, '提示', {
          confirmButtonText: '确定',
          callback: action => {
           router.push({name: 'index'});
            
          },
          
        });*/
        this.$http.post('/api/send_sms',postdata).then(response => {
          response = response.body;
          //var data=response.data;
          //this.$alert(postdata)
          if (response.status==0){
            this.$alert("发送成功", '提示', {
          confirmButtonText: '确定',
          callback: action => {
           router.push({name: 'send_sms'});     
          },
          
        });
          }
          else {
             this.$alert("腾讯云服务已放弃（模板单一，涉及个人隐私），其他服务调研中", '提示', {
          confirmButtonText: '确定',
          /*
            this.$alert("发送失败", '提示', {
          confirmButtonText: '确定',
          callback: action => {
           router.push({name: 'send_sms'});     
          },
          */
        });
          }
        })
        console.log('submit!');
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.all{
  position:absolute;
  background: rgba(0, 0, 0, 0);
  height: 100%;
  width: 100%;
  border:none;  
}
.icon_bar{
  position:absolute;
  background: rgba(0, 0, 0, 0);
  height: 60px;
  width: 120px;
  border:none;  
  text-align: left;
  font-size: x-large;
  font-weight: bold;
  color: palegreen;
}

.configArea{
  position:absolute;
  background: rgba(0, 0, 0, 0);
  margin:20px;
  padding: 10px;
  border: 10px;
  width:80%;
  border:none; 
}
  .conf_title{
    min-height: 50px;
  padding-top: 10px;
  border:none; 
  overflow:auto;
  }
  .selectDiv {
        float: left;
        margin:10px;
        width:330px;
        height:50px;
    }
   .res_div {
        width:500px;
        float: left;
        
    }
 .f_button {
        float: left;
        margin:10px;
        width:330px;
        height:50px;
        left:95%;
        bottom: 10%;
        
    }
.tablelist{
 position:absolute;
  background: rgba(0, 0, 0, 0);
  top:60%;
  width:80%;
   
  border:none; 
}


</style>
