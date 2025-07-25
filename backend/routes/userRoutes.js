const express = require("express");
const router = express.Router();
const User = require("../models/User");

router.post("/", async (req, res) => {
    try {
        const newUser = new User(req.body);
        await newUser.save();
        res.status(201).json({ message: "User saved successfully" });
    } catch (err) {
        res.status(500).json({ error: "Error saving user" });
    }
});

module.exports = router;
