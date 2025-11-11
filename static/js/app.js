// Shopify Search App - Frontend JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const productsGrid = document.getElementById('productsGrid');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const messageContainer = document.getElementById('messageContainer');
    const noResults = document.getElementById('noResults');

    // Handle search button click
    searchButton.addEventListener('click', performSearch);

    // Handle Enter key press in search input
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });

    /**
     * Perform the search by calling the API
     */
    function performSearch() {
        const query = searchInput.value.trim();
        
        if (!query) {
            showMessage('Please enter a search term', 'warning');
            return;
        }

        // Show loading state
        showLoading();
        hideMessage();
        hideNoResults();
        clearProducts();

        // Call the search API
        fetch(`/api/search?query=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                hideLoading();
                
                if (data.products && data.products.length > 0) {
                    showMessage(data.message, 'success');
                    displayProducts(data.products);
                } else {
                    showMessage(data.message || 'No products found', 'info');
                    showNoResults();
                }
            })
            .catch(error => {
                hideLoading();
                showMessage('Error searching products. Please try again.', 'error');
                console.error('Search error:', error);
            });
    }

    /**
     * Display products in the grid
     */
    function displayProducts(products) {
        clearProducts();
        
        products.forEach(product => {
            const productCard = createProductCard(product);
            productsGrid.appendChild(productCard);
        });
    }

    /**
     * Create a product card element
     */
    function createProductCard(product) {
        const card = document.createElement('div');
        card.className = 'product-card';
        
        card.innerHTML = `
            <img src="${product.image}" alt="${product.title}" class="product-image">
            <div class="product-info">
                <h3 class="product-title">${product.title}</h3>
                <p class="product-description">${product.description}</p>
                <div class="product-price">${product.price}</div>
            </div>
        `;
        
        // Add click animation
        card.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 100);
        });
        
        return card;
    }

    /**
     * Clear all products from the grid
     */
    function clearProducts() {
        productsGrid.innerHTML = '';
    }

    /**
     * Show loading spinner
     */
    function showLoading() {
        loadingSpinner.style.display = 'block';
    }

    /**
     * Hide loading spinner
     */
    function hideLoading() {
        loadingSpinner.style.display = 'none';
    }

    /**
     * Show a message to the user
     */
    function showMessage(message, type = 'info') {
        messageContainer.textContent = message;
        messageContainer.style.display = 'block';
        
        // Set color based on type
        const colors = {
            success: '#4CAF50',
            error: '#f44336',
            warning: '#ff9800',
            info: '#2196F3'
        };
        messageContainer.style.color = colors[type] || colors.info;
    }

    /**
     * Hide the message
     */
    function hideMessage() {
        messageContainer.style.display = 'none';
    }

    /**
     * Show no results message
     */
    function showNoResults() {
        noResults.style.display = 'block';
    }

    /**
     * Hide no results message
     */
    function hideNoResults() {
        noResults.style.display = 'none';
    }
});
