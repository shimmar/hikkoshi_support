<template>
  <main>
    <div class="contents">
      <table class="urlTable">
        <tr v-for="(room, index) in roomList" :key="index">
          <th>
            <label :for="'url' + String(index)">候補物件{{ index + 1 }}</label>
          </th>
          <td>
            <input
              type="text"
              :id="'url' + String(index)"
              v-model="room.url"
              @keyup.enter="moveCursor(index)"
            />
          </td>
          <td><button @click="deleteUrl(index)">削除</button></td>
        </tr>
      </table>
    </div>
    <div class="contents">
      <RouterLink to="/result" class="pageMoveButton" @click="moveToShowResultPage()"
        >分析開始</RouterLink
      >
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import { useAppStateStore, useListedRoomsStore } from '../stores/store.js'

let roomList = ref([{ url: '' }])

function moveCursor(index) {
  console.log('current:', index)
  if (index < roomList.value.length - 1) {
    document.getElementById('url' + String(index + 1)).focus()
  } else if (index === roomList.value.length - 1) {
    roomList.value.push({ url: '' })
    document.getElementById('url' + String(index + 1)).focus()
  } else {
    console.log('roomList index ERROR')
  }
}

function deleteUrl(index) {
  roomList.value.splice(index, 1)
}

function moveToShowResultPage() {
  const listedRooms = useListedRoomsStore()
  const appState = useAppStateStore()
  listedRooms.listedRooms = roomList
  appState.progress()
}
</script>

<style scoped>
.urlTable {
  font-size: 2.5vw;
}

.contents {
  width: 30vw;
  margin: auto;
  padding: 2vw;
}
</style>
