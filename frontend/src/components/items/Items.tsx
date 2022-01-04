import { useDispatch, useSelector } from 'react-redux';

import Item from 'components/item/Item';
import ToggleAll from 'components/toggle-all/ToggleAll';
import { remove, toggle } from 'features/items/itemSlice';
import { RootState } from 'features/store';

function Items() {
  const items = useSelector((state: RootState) => state.items.items);
  const dispatch = useDispatch();

  const handleToggle = (id: number) => {
    dispatch(toggle(id));
  };

  const handleRemove = (id: number) => {
    dispatch(remove(id));
  };

  return (
    <section className="main">
      <ul className="todo-list">
        {items.map(item => (
          <Item key={item.id} id={item.id} completed={item.completed} value={item.value} onToggle={handleToggle}
                onRemove={handleRemove} />))}
      </ul>
      <ToggleAll />
    </section>
  );
}

export default Items;