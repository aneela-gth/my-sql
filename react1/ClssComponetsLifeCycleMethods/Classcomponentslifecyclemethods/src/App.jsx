import { MountingPhase } from "./Component/MountingPhase"
import { Unmounting } from "./Component/UnmountingPhase"
import { UpdatingPhase } from "./Component/UpdatingPhase"

function App() {
 

  return (
    <>
     <MountingPhase></MountingPhase>
     <UpdatingPhase></UpdatingPhase>
     <Unmounting></Unmounting>
     
 
    </>
  )
}

export default App
