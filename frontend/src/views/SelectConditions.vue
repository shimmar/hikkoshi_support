<template>
  <main>
    <div class="contents">
      <select v-model="selected" multiple :size="conditions.length + 1">
        <option disabled value="">Ctrlで複数選択</option>
        <option v-for="(con, index) in conditions" :value="con.value" :key="index">
          {{ con.text }}
        </option>
      </select>
    </div>
    <div class="contents">
      <RouterLink to="/list" class="pageMoveButton">決定</RouterLink>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const conditions = [
  { text: '階数', value: 'floor' },
  { text: '間取り', value: 'rooms' },
  { text: '面積', value: 'area' },
  { text: '築年数', value: 'old' },
  { text: '向き', value: 'direction' },
  { text: '駅距離', value: 'distance' },
  { text: '材質', value: 'made_of' }
]
let selected = ref([])
</script>

<style scoped>
select {
  font-size: 2.5vw;
}
.contents {
  width: 30vw;
  margin: auto;
  padding: 2vw;
}
</style>
