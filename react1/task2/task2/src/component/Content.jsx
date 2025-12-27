function Content() {
  return (
    <div style={{ display: "flex", padding: "20px", gap: "10px" }}>
      
      <div style={{ flex: 1, background: "#81827dff", padding: "10px" }}>
        <h3>Left Content</h3>
        <p>This is the left section.</p>
      </div>

      <div style={{ flex: 1, background: "#bbd71eff", padding: "10px", }}>
        <h3>Center Content</h3>
        <p>This is the center section.</p>
      </div>

      <div style={{ flex: 1, background: "#7a7a79ff", padding: "10px" }}>
        <h3>Right Content</h3>
        <p>This is the right section.</p>
      </div>

    </div>
  );
}

export default Content;
