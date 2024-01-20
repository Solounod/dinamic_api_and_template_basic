import axios from 'axios';

const apiSearchProduct = axios.create({
    baseURL: 'http://localhost:8000/api/products/search'
})


export const getSearchProduct = async (search) => {
    const response = await apiSearchProduct.get(`/${search}/`);
    return response.data;
}