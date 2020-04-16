<template>

</template>

<script>
import { breadcrumbs } from './Breadcrumbs'

export default {
  name: 'app-breadcrumbs',
  data () {
    return {
      breadcrumbs: breadcrumbs,
    }
  },
  computed: {
    currentRouteName () {
      return this.$route.name
    },
  },
}

</script>
