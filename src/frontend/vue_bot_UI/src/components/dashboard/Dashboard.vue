<template>
  <div>
    <div class="va-row">
      <div class="flex xs12 md12">
        <vuestic-widget :headerText="$t('Greeting message 招呼訊息')">
          <div class="form-group">
            <div class="input-group">
              <textarea v-model="greeting" id="simple-textarea"  required>add</textarea>
              <label class="control-label" for="simple-textarea">Textarea</label><i class="bar"></i>
            </div>
          </div>

        </vuestic-widget>
      </div>
    </div>

    <div class="va-row">
      <div class="flex xs12 md12">
        <vuestic-widget :headerText="$t('keyword 關鍵字')">
          <div class="va-row">
            <div class="flex md4">
              <fieldset v-for='p in pair'>
                <div class="form-group">
                  <div class="input-group" >
                    <input id="simple-input" v-model=p.k required />
                    <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
                  </div>
                </div>
              </fieldset>
            </div>
            <div class="flex md4">
              <fieldset v-for='p in pair'>
                <div class="form-group">
                  <div class="input-group">
                    <input id="simple-input" v-model=p.r required />
                    <label class="control-label" for="simple-input">Text input</label><i class="bar"></i>
                  </div>
                </div>
              </fieldset>
            </div>
          </div>
          <buttom @click="add" class="btn btn-micro btn-primary">add</buttom>
        </vuestic-widget>
        <buttom @click="save" class="btn btn-micro btn-primary">SAVE</buttom>
        <br>
        <br>
      </div>

    <div class="va-row">
      <div class="flex xs12 md12">
        <vuestic-widget :headerText="$t('')">
          <div class="table-responsive">
            <table class="table table-striped first-td-padding">
              <thead>
              <tr>
                <td>{{'Keyword' | translate}}</td>
                <td>{{'Response' | translate}}</td>
                <td ></td>
              </tr>
              </thead>
              <tbody >
              <tr v-for="i in datatable">
                <td>{{i.k}}</td>
                <td>{{i.r}}</td>
              </tr>
              </tbody>
            </table>
          </div>
        </vuestic-widget>
      </div>
    </div>

    </div>

        
      
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

    name: "dashboard",
    data: function() {
        return {
          datatable: [,,,,,,,,,,,,,],
          greeting: '',
          key: '',
          work: '',
          pair: [{'k':'','r':''}]
        }
    },
    methods: {
      add () {this.pair.push({'k':'','r':''})},
      save () {
        this.$ajax({
        method: 'post',
        url: 'https://sslinebotss.herokuapp.com/handler',
        data: {
        source: 'text',
        grt_msg: this.greeting,
        message: this.pair,
          }
        })
      },
      show_data () {
        const path = 'https://sslinebotss.herokuapp.com/keyword'
          axios.get(path).then(response => {
            this.datatable = response.data
          }).catch(error => {
            console.log(error)
          })

      }
    }
  }
</script>