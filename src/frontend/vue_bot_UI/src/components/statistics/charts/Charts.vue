<template>
  <div class="flex md12">
    <vuestic-widget :headerText="$t('Creat Group')">
      <div class="flex md4">
        <fieldset>
          <div class="form-group">
            <div class="input-group">
              <input id="simple-input" v-model='group_name' required />
              <label class="control-label" for="simple-input">Group name</label><i class="bar"></i>
            </div>
          </div> 
        </fieldset>
      </div>
        <buttom @click="creat" class="btn btn-micro btn-primary">CREAT</buttom>
    </vuestic-widget>

    <vuestic-widget :headerText="$t('Edit Group')">
      <div class="va-row">
        <div class="flex md4">
          <fieldset>
            <div class="form-group">
              <div class="input-group">
                <input id="simple-input" v-model='user_name' required />
                <label class="control-label" for="simple-input">User Name</label><i class="bar"></i>
              </div>
            </div>
          </fieldset>
        </div>
        <div class="flex md4">
          <fieldset>
            <vuestic-simple-select label="group" v-model="target_group" option-key="description" v-bind:options="datatable2" clearable="false" />
          </fieldset>
        </div>
      </div>
        <buttom @click="submit" class="btn btn-micro btn-primary">Submit</buttom>
    </vuestic-widget>
    <div class="va-row">
      <div class="flex xs12 md12">
        <vuestic-widget :headerText="$t('')">
          <div class="table-responsive">
            <table class="table table-striped first-td-padding">
              <thead>
              <tr>
                <td>{{'USERNAME' | translate}}</td>
                <td>{{'USERID' | translate}}</td>
                <td ></td>
              </tr>
              </thead>
              <tbody >
              <tr v-for="i in datatable">
                <td>{{i.name}}</td>
                <td>{{i.id}}</td>
              </tr>
              </tbody>
            </table>
          </div>
        </vuestic-widget>
      </div>
    </div>

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
              <tr v-for="i in datatable3">
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
  name: 'charts',
  components: {
  },
  data () {
    return{
    user_name:'',
    target_group:'',
    group_name:'',
    datatable:[,,,,,,,,],
    datatable2:[,,,,,,,,],
    datatable3:[,,,,,,,,],
  }},
  methods: {
    creat () {
      this.$ajax({
        method: 'post',
        url: 'https://sslinebotss.herokuapp.com/handler',
        data: {
        source: 'group',
        group_name: this.group_name,
        }
      })
    },

    submit () {
      this.$ajax({
        method: 'post',
        url: 'https://sslinebotss.herokuapp.com/handler',
        data: {
        source: 'edit',
        group_name: this.target_group,
        user: this.user_name,
        }
      })
    },

    show_data () {
      const path = 'https://sslinebotss.herokuapp.com/user'
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
      const path3 = 'https://sslinebotss.herokuapp.com/groperson'
      axios.get(path3).then(response => {
          this.datatable3 = response.data
        }).catch(error => {
          console.log(error)
        })
    },
  },
}
</script>

<style lang="scss">
.widget.chart-widget {
  .widget-body {
    height: 550px;
  }
}
</style>
