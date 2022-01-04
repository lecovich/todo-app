import Header from 'components/header/Header';
import Footer from 'components/footer/Footer';
import Items from 'components/items/Items';

function App() {
  return (
    <section className="todoapp">
      <Header />
      <Items />
      <Footer />
    </section>
  );
}

export default App;
