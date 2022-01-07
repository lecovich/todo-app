import Item from 'components/item/Item';
import ToggleAll from 'components/toggle-all/ToggleAll';
import { useGetAllItemsQuery, useToggleItemMutation } from 'api/items-service';

function Items() {
  const { data } = useGetAllItemsQuery('');

  const [toggleItem] = useToggleItemMutation();

  const handleToggle = (id: string, completed: boolean) => {
    toggleItem({ id, completed });
  };

  const handleRemove = (id: string) => {
    // dispatch(remove(id));
  };

  return (
    <section className="main">
      <ul className="todo-list">
        {data?.map(item => (
          <Item key={item.id} id={item.id} completed={item.completed} value={item.value} onToggle={handleToggle}
                onRemove={handleRemove} />))}
      </ul>
      <ToggleAll />
    </section>
  );
}

export default Items;