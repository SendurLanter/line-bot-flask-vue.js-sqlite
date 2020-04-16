<template>
  <div class="form-wizard-page">
    <div class="va-row">
      <div class="flex md12">
        <vuestic-widget class="no-h-padding"
                        :headerText="$t(

                        'add text here'

                        )">
          <vuestic-wizard
            :steps="hsSteps">
            <div slot="page1" class="form-wizard-tab-content">
              <div class="form-wizard-tab-content-text">
                <p>

                add text here!

                </p>
              </div>
              <div class="form-group with-icon-right"
                   :class="{'has-error': errors.has('hsName'), 'valid': isFormFieldValid('hsName')}">
                <div class="input-group">
                  <input
                    name="hsName"
                    data-vv-as="Name"
                    v-model="hsName"
                    v-validate="'required'"
                    required title=""/>
                  <i
                    class="fa fa-exclamation-triangle error-icon icon-right input-icon"></i>
                  <i class="fa fa-check valid-icon icon-right input-icon"></i>
                  <label class="control-label">{{

                  'abcdefghijk'
                  |
                    translate}}</label><i class="bar"></i>
                  <small v-show="errors.has('hsName')" class="help text-danger">
                    {{ errors.first('hsName') }}
                  </small>
                </div>
              </div>
            </div>
            <div slot="page2" class="form-wizard-tab-content">
              <div class="form-wizard-tab-content-text">
                <p>

                add text here

                </p>
              </div>
              <vuestic-simple-select
                label="Select"
                v-model="hsCountry"
                name="country"
                ref="hsCountrySelect"
                v-bind:options="countriesList"
                >
              </vuestic-simple-select>
            </div>
            <div slot="page3" class="form-wizard-tab-content">
              <h4>{{'forms.wizard.confirmSelection' | translate}}</h4>
              <p>

              add text here              

              </p>
            </div>
            <div slot="wizardCompleted" class="form-wizard-tab-content">
              <h4>{{'forms.wizard.completed' | translate}}</h4>
              <p>???
              </p>
            </div>
          </vuestic-wizard>
        </vuestic-widget>
      </div>
    </div>
  </div>
</template>

<script>
import CountriesList from 'data/CountriesList'
import axios from 'axios';
export default {
  name: 'form-wizard',

  computed: {
    hsSteps () {
      return [
        {
          label: this.$t('~~1~~'),
          slot: 'page1',
          onNext: () => {
            this.hi()
          },
          isValid: () => {
            return this.isFormFieldValid('hsName')
          },
        },
        {
          label: this.$t('~~2~~'),
          slot: 'page2',
          onNext: () => {
            this.$refs.hsCountrySelect.validate()
          },
          isValid: () => {
            return this.$refs.hsCountrySelect.isValid()
          },
        },
        {
          label: this.$t('forms.wizard.stepThree'),
          slot: 'page3',
        },
      ]
    },
    hrSteps () {
      return [
        {
          label: this.$t('forms.wizard.stepOne'),
          slot: 'page1',
          onNext: () => {
            this.hi()
          },
          isValid: () => {
            return this.isFormFieldValid('hrName')
          },
        },
        {
          label: this.$t('forms.wizard.stepTwo'),
          slot: 'page2',
          onNext: () => {
            this.$refs.hrCountrySelect.validate()
          },
          isValid: () => {
            return this.$refs.hrCountrySelect.isValid()
          },
        },
        {
          label: this.$t('forms.wizard.stepThree'),
          slot: 'page3',
        },
      ]
    },
    vrSteps () {
      return [
        {
          label: this.$t('forms.wizard.stepOne'),
          slot: 'page1',
          onNext: () => {
            this.hi()
          },
          isValid: () => {
            return this.isFormFieldValid('vrName')
          },
        },
        {
          label: this.$t('forms.wizard.stepTwo'),
          slot: 'page2',
          onNext: () => {
            this.$refs.vrCountrySelect.validate()
          },
          isValid: () => {
            return this.$refs.vrCountrySelect.isValid()
          },
        },
        {
          label: this.$t('forms.wizard.stepThree'),
          slot: 'page3',
        },
      ]
    },
    vsSteps () {
      return [
        {
          label: this.$t('forms.wizard.stepOne'),
          slot: 'page1',
          onNext: () => {
            this.hi()
          },
          isValid: () => {
            return this.isFormFieldValid('vsName')
          },
        },
        {
          label: this.$t('forms.wizard.stepTwo'),
          slot: 'page2',
          onNext: () => {
            this.$refs.vsCountrySelect.validate()
          },
          isValid: () => {
            return this.$refs.vsCountrySelect.isValid()
          },
        },
        {
          label: this.$t('forms.wizard.stepThree'),
          slot: 'page3',
        },
      ]
    },
  },
  data () {
    return {
      hsName: '',
      hsCountry: '',
      hrName: '',
      hrCountry: '',
      vrName: '',
      vrCountry: '',
      vsName: '',
      vsCountry: '',
      email: '',
      countriesList: CountriesList,
      chosenCountry: '',
    }
  },
  methods: {
    isFormFieldValid (field) {
      let isValid = false
      if (this.formFields[field]) {
        isValid = this.formFields[field].validated && this.formFields[field].valid
      }
      return isValid
    },
    validateFormField (fieldName) {
      this.$validator.validate(fieldName, this[fieldName])
    },

    hi () {
    this.$ajax({
      method: 'post',
      url: 'http://127.0.0.1:5000/handler',
      data: {
      name: 'wise',
      info: 'wrong'
      }
    })
  },
}
}
</script>

<style lang="scss">
.widget.simple-vertical-wizard-widget {
  .widget-body {
    padding: 0 $widget-padding;
    @include media-breakpoint-down(sm) {
      padding: $widget-padding 0;
    }
  }
}
</style>
