const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
    firstName: String,
    lastName: String,
    email: String,
    dob: String,
    country: String,
    state: String,
    gender: String
});

module.exports = mongoose.model("User", userSchema);
