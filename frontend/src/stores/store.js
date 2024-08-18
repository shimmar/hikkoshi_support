import { defineStore } from 'pinia'

const APPSTATES = Object.freeze({
  SELECTCONDITIONS: 1,
  LISTROOMS: 2,
  RESULT: 3
})

export const useAppStateStore = defineStore('appState', {
  state: () => ({
    appState: 1
  }),
  getters: {
    isLaterThan(destination) {
      const destinationInt = APPSTATES[destination]
      return this.appState > destinationInt
    }
  },
  actions: {
    progress() {
      if (this.appState < APPSTATES['RESULT']) {
        this.appState++
      } else if (this.appState === APPSTATES['RESULT']) {
        this.appState = APPSTATES['SELECTCONDITIONS']
      } else {
        console.log('invalid appState value')
      }
      console.log('Progress: ', this.appState)
    },
    jumpTo(destination) {
      if (this.isLaterThan(destination)) {
        this.appState = APPSTATES[destination]
      }
      console.log('Jump to: ', this.appState)
    }
  }
})

export const useSelectedConditionsStore = defineStore('selectedConditions', {
  state: () => ({
    /** @type {String[]} */
    selectedConditions: []
  }),
  actions: {
    clear() {
      this.selectedConditions = []
    }
  }
})

export const useListedRoomsStore = defineStore('listedRooms', {
  state: () => ({
    /** @type {{url:string}[]} */
    listedRooms: []
  }),
  actions: {
    clear() {
      this.listedRooms = []
    }
  }
})
