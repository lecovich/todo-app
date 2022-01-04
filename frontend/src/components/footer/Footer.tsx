function Footer() {
  return (
    <div className="footer">
      <span className="todo-count"/>
      <ul className="filters">
        <li>
          <a href="#/" className="selected">All</a>
        </li>
        <li>
          <a href="#/active">Active</a>
        </li>
        <li>
          <a href="#/completed">Completed</a>
        </li>
      </ul>
      <button className="clear-completed">Clear completed</button>
    </div>
  )
}

export default Footer;