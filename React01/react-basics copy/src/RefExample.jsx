import React, { useRef } from "react";
function RefExample() {
  const inputRef = useRef(null);
  function focusInput() {
    inputRef.current.focus();
  }
  return (
    <div>
      <h3>Ref Example</h3>
      <input type="text" ref={inputRef} placeholder="Click button to focus me" />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
}

export default RefExample;