const resultHit = (hit, { html, sendEvent }) => html`
  <div class="result-hit__image-container">
    <div>
      <img
        class="result-hit__image"
        src="${hit.image}"
        align="left"
        alt="${hit.name}"
      />
      <div class="result-hit__details">
        <h3 class="result-hit__name">${hit.name}</h3>
        <p class="result-hit__price">$${hit.price}</p>
      </div>
    </div>
    <div class="result-hit__controls">
      <button
        id="view-item"
        class="result-hit__view"
        onclick="${(evt) => {
          evt.stopPropagation();
          sendEvent('click', hit, 'View Product');
        }}"
      >
        View Product
      </button>
      <button
        id="add-to-cart"
        class="result-hit__cart"
        onclick="${(evt) => {
          evt.stopPropagation();
          sendEvent('conversion', hit, 'Add Product To Cart');
        }}"
      >
        Add To Cart
      </button>
    </div>
  </div>
`;

export default resultHit;
