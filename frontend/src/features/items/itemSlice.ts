import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface Item {
  completed: boolean;
  value: string;
  id: number;
}

export interface ItemState {
  items: Item[];
}

const initialState: ItemState = {
  items: [
    { id: 1, value: 'foo', completed: false },
    { id: 2, value: 'bar', completed: true },
  ]
};

export const itemsSlice = createSlice({
  name: 'items',
  initialState,
  reducers: {
    toggle: (state, action: PayloadAction<number>) => {
      const id = action.payload;
      state.items = state.items.map(item => item.id === id ? { ...item, completed: !item.completed } : item);
    },
    remove: (state, action: PayloadAction<number>) => {
      const id = action.payload;
      state.items = state.items.filter(item => item.id !== id);
    },
  },
});

export const { toggle, remove } = itemsSlice.actions;

export default itemsSlice.reducer;