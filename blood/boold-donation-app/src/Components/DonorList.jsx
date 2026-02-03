function DonorList({ blood, location, setSelectedDonor }) {
  const donors = JSON.parse(localStorage.getItem("donors")) || [];

  const filtered = donors.filter(
    (d) => d.blood === blood && d.location === location
  );

  if (!blood || !location) return null;

  return (
    <>
      <h3>Available Donors</h3>

      {filtered.length === 0 ? (
        <p>No donors found</p>
      ) : (
        filtered.map((d, i) => (
          <div className="card" key={i}>
            <p><b>Name:</b> {d.name}</p>
            <p><b>Blood:</b> {d.blood}</p>
            <p><b>Location:</b> {d.location}</p>

            <button onClick={() => setSelectedDonor(d)}>
              Request Blood
            </button>
          </div>
        ))
      )}
    </>
  );
}

export default DonorList;
