<template>
  <div class="header">
    <div>
      <h1>引っ越し先選び</h1>
    </div>
    <div class="flow">
      <RouterLink to="/">条件</RouterLink>→ <RouterLink to="/">候補</RouterLink>→
      <RouterLink to="/">結果</RouterLink>
    </div>
  </div>
</template>

<style scoped>
.header {
  display: flex;
}

.flow {
  font-size: 20px;
  margin-left: auto;
}
</style>
