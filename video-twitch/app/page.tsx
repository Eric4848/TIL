import { Button } from "@/components/ui/button";
import Image from "next/image";

export default function Home() {
  return (
    <div>
      <p className='text-red-500 font-bold'>Hello Twitch Clone</p>
      <Button size="lg" variant="outline">
        Click me!
      </Button>
    </div>
  );
}