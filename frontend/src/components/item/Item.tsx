import classNames from 'classnames';
import { FunctionComponent } from 'react';

interface ItemProps {
  id: string;
  value: string;
  completed: boolean;
  onToggle?: (id: string, completed: boolean) => void;
  onRemove?: (id: string) => void;
}

const Item: FunctionComponent<ItemProps> = ({ id, value, completed, onToggle, onRemove }) => {
  const itemClassName = classNames({ completed: completed });

  return (
    <li className={itemClassName}>
      <div className="view">
        <input className="toggle" type="checkbox" defaultChecked={completed} onClick={() => {
          onToggle && onToggle(id, !completed);
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