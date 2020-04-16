<template>
  <vuestic-sidebar :hidden="isOpen">
    <template slot="menu">

      <sidebar-link
        :to="{ name: 'dashboard' }">
        <span slot="title">
          <span class="sidebar-menu-item-icon vuestic-icon vuestic-icon-dashboard"></span>
          <span>{{ $t('Message') }}</span>
        </span>
      </sidebar-link>

      <sidebar-link
          :to="{ name: 'charts' }">
          <span slot="title">
            <span class="sidebar-menu-item-icon vuestic-icon vuestic-icon-statistics"></span>
          <span>{{ $t('Groups') }}</span>
        </span>
            <span>{{ $t('menu.charts') }}</span>
          </span>
      </sidebar-link>

      <sidebar-link
        :to="{ name: 'medium-editor' }">
        <span slot="title">
        <span class="sidebar-menu-item-icon vuestic-icon vuestic-icon-forms"></span>
          <span>{{ $t('Push') }}</span>
        </span>
      </sidebar-link>

      <sidebar-link
        :to="{ name: 'tables' }">
        <span slot="title">
          <span
            class="sidebar-menu-item-icon vuestic-icon vuestic-icon-tables"></span>
          <span>{{ $t('Creat Menu') }}</span>
        </span>
      </sidebar-link>

      <sidebar-link
        :to="{ name: 'extra' }">
        <span slot="title">
          <span
            class="sidebar-menu-item-icon vuestic-icon vuestic-icon-extras"></span>
          <span>{{ $t('Hierachy') }}</span>
        </span>
      </sidebar-link>

    </template>
  </vuestic-sidebar>
</template>

<script>

import VuesticSidebar
  from '../../../vuestic-theme/vuestic-components/vuestic-sidebar/VuesticSidebar'
import SidebarLink from './components/SidebarLink'
import SidebarLinkGroup from './components/SidebarLinkGroup'

export default {
  name: 'app-sidebar',
  components: {
    VuesticSidebar,
    SidebarLink,
    SidebarLinkGroup,
  },
  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
}

</script>
