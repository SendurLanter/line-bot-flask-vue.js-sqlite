<template>
  <div class="flex md12">
    <vuestic-widget :headerText="$t('Push')">
      <div class="flex md4">
        <fieldset>
          <fieldset>
            <vuestic-simple-select label="group" v-model="target_group" option-key="description" v-bind:options="datatable2" clearable="false" />
          </fieldset>
        </fieldset>
      </div>
      <br>
        <fieldset>

          <div class="form-group">
            <div class="input-group">
              <textarea v-model="content" id="simple-textarea"  required></textarea>
              <label class="control-label" for="simple-textarea">broadcast</label><i class="bar"></i>
            </div>
          </div>
        
        </fieldset>
    </vuestic-widget>

      <buttom @click="send" class="btn btn-micro btn-primary">SEND</buttom>
    <br>
    <br>

    <div class="va-row">
      <div class="flex xs12 md12">
        <vuestic-widget :headerText="$t('')">
          <div class="table-responsive">
            <table class="table table-striped first-td-padding">
              <thead>
              <tr>
                <td>{{'Person_name' | translate}}</td>
                <td>{{'Group_name' | translate}}</td>
                <td></td>
              </tr>
              </thead>
              <tbody>
              <tr v-for="i in datatable">
                <td>{{i.person}}</td>
                <td>{{i.group_name}}</td>
                
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
  name: 'medium-editor',

  data () {
    return {
      datatable: [,,,,,,,,,,,,,],
      datatable2: [,,,,,,,,,,,,],
      group: '',
      content: '',
      target_group:'',
  }},

  methods: {
    send () {
      this.$ajax({
        method: 'post',
        url: 'https://sslinebotss.herokuapp.com/handler',
        data: {
        source: 'push',
        target: this.target_group,
        message: this.content,
        }
      })
    },
    show_data () {
        const path = 'https://sslinebotss.herokuapp.com/groperson'
          axios.get(path).then(response => {
            this.datatable = response.data
          }).catch(error => {
            console.log(error)
          })
        const path2 = 'https://sslinebotss.herokuapp.com/group'
          axios.get(path2).then(response => {
            this.datatable2 = response.data
          }).catch(error => {
            console.log(error)
          })

      },
  }
}

</script>
<style lang="scss">

</style>
