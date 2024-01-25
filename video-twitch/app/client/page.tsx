"use client"

const Test = () => {
  const onClick = () => {
    console.log("clicked")
  }
  return (
    <div onClick={onClick}>
      Client Test
    </div>
  )
}

export default Test