<template>
  <div class="va-row dashboard-info-widgets">
    <div class="flex md6 xl3 xs12">

    </div>
  </div>
</template>

<script>
export default {
  name: 'dashboard-info-widgets',
}
</script>

<style lang="scss" scoped>
.stats-number, .stats-title {
  line-height: 1;
}

.info-widget-inner {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;

  &.has-chart {
    justify-content: space-between;
  }

  .stats {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
  }
}

.stats-number {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  font-size: 2.625rem;
  margin-bottom: 0.5rem;

  .stats-icon {
    font-size: 1.5625rem;
    position: absolute;
    top: 0.625rem;
    left: -1.25rem;

    &.icon-wide {
      left: -1.875rem;
    }
  }
}

</style>
