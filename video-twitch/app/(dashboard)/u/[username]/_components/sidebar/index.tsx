import { Navigation } from "./navigation";
import { Toggle } from "./toggle";
import { Wrapper } from "./wrapper";

export const Sidbar = () => {
  return (
    <Wrapper>
      <Toggle />
      <Navigation />
    </Wrapper>
  );
};
