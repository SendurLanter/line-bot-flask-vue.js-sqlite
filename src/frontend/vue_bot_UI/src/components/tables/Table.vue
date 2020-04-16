<template>
  <div class="flex md12">
    <vuestic-widget :headerText="$t('Menu name 選單名稱')">
      <div class="form-group">
        <div class="input-group">
          <input id="simple-input" v-model="menu_name" required/>
          <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
        </div>
      </div>
    </vuestic-widget>
    <vuestic-widget :headerText="$t('Background 背景圖片')">
      <form action="https://sslinebotss.herokuapp.com/upload" method="post" enctype="multipart/form-data" target="id_iframe">
        <input type="file" name="file"/>
        <input id="submit_form" type="submit" class="btn btn-primary btn-micro mb-1" value="upload"/>
      </form>
      <iframe id="id_iframe" name="id_iframe" style=""></iframe>
    </vuestic-widget>

    <vuestic-widget :headerText="$t('Actions 觸發動作')">
      <form>
      <div class="va-row">
        <div class="flex md4">
          <fieldset>
            <vuestic-simple-select label="buttom 1 type" v-model="one" option-key="description" v-bind:options="simpleOptions" clearable="false" />
            <vuestic-simple-select label="buttom 2 type" v-model="two" option-key="description" v-bind:options="simpleOptions" clearable="false" />
            <vuestic-simple-select label="buttom 3 type" v-model="three" option-key="description" v-bind:options="simpleOptions" clearable="false" />
            <vuestic-simple-select label="buttom 4 type" v-model="four" option-key="description" v-bind:options="simpleOptions" clearable="false" />
            <vuestic-simple-select label="buttom 5 type" v-model="five" option-key="description" v-bind:options="simpleOptions" clearable="false" />
            <vuestic-simple-select label="buttom 6 type" v-model="six" option-key="description" v-bind:options="simpleOptions" clearable="false" />
          </fieldset>
        </div>
        <div class="flex md4">
          <fieldset>
            <div class="form-group">
              <div class="input-group">
                <input id="simple-input" v-model='a1' required />
                <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
              </div>
            </div> 
            <div class="form-group">
              <div class="input-group">
                <input id="simple-input" v-model='a2' required/>
                <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
              </div>
            </div> 
            <div class="form-group">
              <div class="input-group">
                <input id="simple-input" v-model='a3' required/>
                <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
              </div>
            </div> 
            <div class="form-group">
              <div class="input-group">
                <input id="simple-input" v-model='a4' required/>
                <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
              </div>
            </div> 
            <div class="form-group">
              <div class="input-group">
                <input id="simple-input" v-model='a5' required/>
                <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
              </div>
            </div> 
            <div class="form-group">
              <div class="input-group">
                <input id="simple-input" v-model='a6' required/>
                <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
              </div>
            </div> 
          </fieldset>
        </div>
      </div>
    </form>
    </vuestic-widget>
    
      <buttom @click="save" class="btn btn-micro btn-primary">CREAT</buttom>

    <br>
    <br>

    <div class="va-row">
      <div class="flex xs12 md12">
        <vuestic-widget :headerText="$t('')">
          <div class="table-responsive">
            <table class="table table-striped first-td-padding">
              <thead>
              <tr>
                <td>{{'menu_name' | translate}}</td>
                <td>{{'buttom' | translate}}</td>
                <td>{{'action' | translate}}</td>
                <td></td>
              </tr>
              </thead>
              <tbody>
              <tr v-for="i in datatable">
                <td>{{i.name}}</td>
                <td>{{i.buttom}}</td>
                <td>{{i.action}}</td>
              </tr>

              </tbody>
            </table>
          </div>
        </vuestic-widget>
      </div>
    </div>

  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    created() {
      this.show_data()
    },
    name: "table",
    data: function() {
      return {
      datatable: [,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,],
      test: '',
      menu_name: '',
      single: [],
      one: '',
      two: '',
      three: '',
      four: '',
      five: '',
      six: '',
      a1: '',
      a2: '',
      a3: '',
      a4: '',
      a5: '',
      a6: '',
      simpleOptions: [
      {
        description: 'message',
      },
      {
        description: 'uri',
      },
      {
        description: 'POST',
      },
    ],
      }
  },
  methods: {
    save () {
      this.$ajax({
      method: 'post',
      url: 'https://sslinebotss.herokuapp.com/handler',
      data: {
        source: 'menu',
        name: this.menu_name,
        buttom1: {'type': this.one['description'],'action':this.a1},
        buttom2: {'type': this.two['description'],'action':this.a2},
        buttom3: {'type': this.three['description'],'action':this.a3},
        buttom4: {'type': this.four['description'],'action':this.a4},
        buttom5: {'type': this.five['description'],'action':this.a5},
        buttom6: {'type': this.six['description'],'action':this.a6},
        }
      })
    },
    show_data () {
      const path = 'https://sslinebotss.herokuapp.com/menu'
        axios.get(path).then(response => {
          this.datatable = response.data
        }).catch(error => {
          console.log(error)
        })
    }
  }
}
</script>