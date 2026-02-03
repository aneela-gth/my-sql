import DonorDashboard from "./DonorDashboard";
import RequestBlood from "./RequestBlood";

function Dashboard() {
  const user = JSON.parse(localStorage.getItem("currentUser"));

  return (
    <div className="container">
      <h2>Welcome {user.name}</h2>
      {user.role === "donor" ? <DonorDashboard user={user} /> : <RequestBlood />}
    </div>
  );
}

export default Dashboard;
