import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

import { Item } from 'shared/types';

export const itemsApi = createApi({
  reducerPath: 'itemsApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:8000/api/' }),
  tagTypes: ['Items'],
  endpoints: (builder) => ({
    getAllItems: builder.query<Item[], string>({
      query: () => `items`,
      providesTags: ['Items'],
    }),
    toggleItem: builder.mutation<Item, Partial<Item> & Pick<Item, 'id'>>({
      query: ({ id, ...body }) => ({
        url: `items/${id}`,
        method: 'PUT',
        body,
      }),
      invalidatesTags: ['Items'],
    })
  }),
});

export const { useGetAllItemsQuery, useToggleItemMutation } = itemsApi;