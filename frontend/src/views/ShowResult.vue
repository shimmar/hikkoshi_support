<template>
  <main>
    <div class="contents">
      <table>
        <tr>
          <th>物件名</th>
          <th v-for="con in selected" :key="con">{{ con }}</th>
          <th>家賃</th>
        </tr>
      </table>
    </div>
    <div class="contents">
      <RouterLink to="/" class="pageMoveButton" @click="moveToSelectConditionsPage()"
        >終了</RouterLink
      >
    </div>
  </main>
</template>

<script setup>
import {
  useAppStateStore,
  useSelectedConditionsStore,
  useListedRoomsStore
} from '../stores/store.js'

const appState = useAppStateStore()
const selectedConditions = useSelectedConditionsStore()
const listedRooms = useListedRoomsStore()
const selected = selectedConditions.selectedConditions

function moveToSelectConditionsPage() {
  appState.progress()
  selectedConditions.clear()
  listedRooms.clear()
}
</script>

<style scoped>
.contents {
  width: 30vw;
  margin: auto;
  padding: 2vw;
}
</style>
