import classNames from 'classnames';
import { FunctionComponent } from 'react';

interface ItemProps {
  id: number;
  value: string;
  completed: boolean;
  onToggle?: (id: number) => void;
  onRemove?: (id: number) => void;
}

const Item: FunctionComponent<ItemProps> = ({ id, value, completed, onToggle, onRemove }) => {
  const itemClassName = classNames({ completed: completed });

  return (
    <li className={itemClassName}>
      <div className="view">
        <input className="toggle" type="checkbox" defaultChecked={completed} onClick={() => {
          onToggle && onToggle(id);
        }} />
        <label>{value}</label>
        <button className="destroy" onClick={() => {
          onRemove && onRemove(id);
        }} />
      </div>
    </li>
  );
};

export default Item;