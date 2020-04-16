<template>
  <div class="flex md12">
    <div class="va-row">
      <div class="flex xs12 md12">
        <vuestic-widget :headerText="$t('Linked User Name 對應的使用者')">
        <div class="flex md4">
          <div class="form-group">
            <div class="input-group">
              <input id="simple-input" v-model='id' required />
              <label class="control-label" for="simple-input">Name</label><i class="bar"></i>
            </div>
          </div>
        </div>
        </vuestic-widget>
      </div>
    </div> 
    </br> 

    <vuestic-widget :headerText="$t('Hierachy 階層式選單')">
      <vuestic-tree-root>
      <div class="flex md2">
      <div class="form-group">
        <div class="input-group">
          <input v-model='main'>
          <i class="bar"></i>
        </div>              
     </div>
     </div>
        <vuestic-tree-category >

          <vuestic-tree-node v-for="l1 in L1":key="l1.id">
            <div class="flex md1">
              <div class="form-group">
                <div class="input-group">
                  <input v-model=l1.name>
                  <i class="bar"></i>
               </div>              
              </div>
            </div>

            <vuestic-tree-category>
              <vuestic-tree-node v-for="l2 in L2":key="l2.id">
                <div class="flex md1">
                <div class="form-group">
                  <div class="input-group">
                    <input v-model=l2.name>
                    <i class="bar"></i>
                  </div>              
                </div>
                </div>
                <vuestic-tree-category>
                  <vuestic-tree-node v-for="l3 in L3":key="l3.id">
                    <div class="flex md1">
                    <div class="form-group">
                      <div class="input-group">
                        <input v-model=l3.name>
                        <i class="bar"></i>
                     </div>              
                    </div>
                    </div>
                  <vuestic-tree-category>

                  </vuestic-tree-category>
                </vuestic-tree-node>
                </vuestic-tree-category>
              </vuestic-tree-node>
            </vuestic-tree-category>

          </vuestic-tree-node>
          <br>
          <button class="btn btn-primary btn-micro mb-1"@click="add2()">add layer</button>
        </vuestic-tree-category>
        <br>
          <button class="btn btn-primary btn-micro mb-1"@click="add1()">add layer</button>
      </vuestic-tree-root>
    </vuestic-widget>
  <buttom @click="save" class="btn btn-primary btn-micro mb-1">SAVE</buttom>  
  <br>
  <br>
    <div class="va-row">
      <div class="flex xs12 md12">
        <vuestic-widget :headerText="$t('')">
          <div class="table-responsive">
            <table class="table table-striped first-td-padding">
              <thead>
              <tr>
                <td>{{'Menu name' | translate}}</td>
                <td>{{'Menu id' | translate}}</td>
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
  </div>
</template>

<script>
import axios from 'axios';
export default {

  created() {
    this.show_data()
  },
  name: 'extra',
  data () {
    return {
      datatable: [,,,,,,,,,,,,,,,,,,,],
      main: 'main_menu',
      L1  : [{ id: 1, name: 'buttom' },{ id: 2, name: 'buttom' },{ id: 3, name: 'buttom' },{ id: 4, name: 'buttom' },{ id: 5, name: 'buttom' },{ id: 6, name: 'buttom' }],
      L2: [],
      L3: [],
      L4: [],
      L5: [],
      }
    },

  methods: {
    add1 () {this.L2.push({ id: 1, name: 'buttom' },{ id: 2, name: 'buttom' },{ id: 3, name: 'buttom' },{ id: 4, name: 'buttom' },{ id: 5, name: 'buttom' },{ id: 6, name: 'buttom' })},
    add2 () {this.L3.push({ id: 1, name: 'buttom' },{ id: 2, name: 'buttom' },{ id: 3, name: 'buttom' },{ id: 4, name: 'buttom' },{ id: 5, name: 'buttom' },{ id: 6, name: 'buttom' })},
    remove1 (product) {
      this.products = this.products.filter(productToFilter => productToFilter !== product)
    },
    save () {
      this.$ajax({
      method: 'post',
      url: 'https://sslinebotss.herokuapp.com/handler',
      data: {
      source: 'hierachy',
      userId: this.id,
      main: this.main,
      L1: this.L1,
      L2: this.L2,
      L3: this.L3,
          }
        })
    },
    show_data () {
      const path = 'https://sslinebotss.herokuapp.com/menu_id'
        axios.get(path).then(response => {
          this.datatable = response.data
        }).catch(error => {
          console.log(error)
        })
      },
  }
}
</script>

<style scoped>

</style>