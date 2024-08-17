<template>
  <div class="header">
    <div id="title">引っ越し先選び</div>
    <div class="flow">
      <RouterLink to="/">条件</RouterLink>→ <RouterLink to="/list">候補</RouterLink>→
      <RouterLink to="/">結果</RouterLink>
    </div>
  </div>
</template>

<style scoped>
.header {
  display: flex;
  padding: 2vw;
}
#title {
  font-size: 3.5vw;
}
.flow {
  font-size: 2vw;
  margin-left: auto;
  vertical-align: middle;
  display: inline-block;
}
</style>
