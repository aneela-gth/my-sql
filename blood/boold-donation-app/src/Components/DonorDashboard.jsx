function DonorDashboard({ user }) {
  return (
    <div className="card">
      <h3>Donor Dashboard</h3>
      <p><b>Blood:</b> {user.blood}</p>
      <p><b>Location:</b> {user.location}</p>
      <p><b>Hospital:</b> {user.hospital}</p>
      <p>Status: Available ❤️</p>
    </div>
  );
}

export default DonorDashboard;
