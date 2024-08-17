<template>
  <main>
    <div class="contents">
      <div v-for="(room, index) in roomList" :key="index">
        <input
          type="text"
          :id="'url' + String(index)"
          v-model="room.url"
          @keyup.enter="moveCursor(index)"
        /><button @click="deleteUrl(index)">削除</button>
      </div>
    </div>
    <div class="contents">
      <RouterLink to="/" class="pageMoveButton">分析開始</RouterLink>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'

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
