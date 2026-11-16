const express = require('express');
const app = express();
app.use(express.json());
let products = [
    {id:1,name:'laptop',price:75000},
    {id:2,name:'mouse',price:500},
    {id:3,name:'keyboard',price:1200}
];
let nextid=4;
app.get('/product',(req,res)=>{
    res.json(products);
})
app.post('/products',(req,res)=>{
    const product={
        id:nextid++,
        name:req.body.name,
        price:req.body.price
    };
    products.push(products);
    res.status.push(product);
    res.status(201).json(product);
});
app.listen(3000,()=>{
    console.log('Server running on port 3000');
})