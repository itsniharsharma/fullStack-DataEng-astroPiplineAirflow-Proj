const express = require('express');
const app = express();
const mongoose = require('mongoose');
const userRoutes = require('./routes/userRoutes');
const cors = require('cors');

app.use(cors());
app.use(express.json()); // important to parse JSON body

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
.then(() => console.log("MongoDB connected"))
.catch((err) => console.error("MongoDB connection error:", err));

app.use('/api/users', userRoutes);

app.listen(5000, () => {
    console.log("Server is running on port 5000");
});
