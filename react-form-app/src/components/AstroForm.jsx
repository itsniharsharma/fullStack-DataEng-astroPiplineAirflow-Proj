import React, { useState } from 'react';
import axios from 'axios';

const AstroForm = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    dob: '',
    email: '',
    country: '',
    state: '',
    gender: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:5000/api/users", formData);

      if (response.status === 200 || response.status === 201) {
        alert("User saved successfully!");
        console.log("Response:", response.data);

        // Optional: Reset form
        setFormData({
          firstName: '',
          lastName: '',
          dob: '',
          email: '',
          country: '',
          state: '',
          gender: '',
        });
      } else {
        alert("Unexpected server response.");
        console.log("Unexpected status:", response.status);
      }
    } catch (err) {
      console.error("Error during form submission:", err);
      alert("Failed to save user. Check console for error.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="astro-form">
      <h2>User Birth Details</h2>

      <label>
        First Name:
        <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} required />
      </label>

      <label>
        Last Name:
        <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} required />
      </label>

      <label>
        Date of Birth:
        <input type="date" name="dob" value={formData.dob} onChange={handleChange} required />
      </label>

      <label>
        Email:
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />
      </label>

      <label>
        Country:
        <input type="text" name="country" value={formData.country} onChange={handleChange} required />
      </label>

      <label>
        State:
        <input type="text" name="state" value={formData.state} onChange={handleChange} required />
      </label>

      <label>
        Gender:
        <select name="gender" value={formData.gender} onChange={handleChange} required>
          <option value="">-- Select Gender --</option>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
          <option value="Other">Other</option>
        </select>
      </label>

      <button type="submit">Submit</button>
    </form>
  );
};

export default AstroForm;
