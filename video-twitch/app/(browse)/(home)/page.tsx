import { Button } from "@/components/ui/button";
import Image from "next/image";
import { UserButton } from "@clerk/nextjs";

export default function Home() {
  return (
    <div className='flex flex-col gap-y-4'>
      <h1>Dashboard</h1>
      <UserButton afterSignOutUrl='/' />
      <p className='text-red-500 font-bold'>Hello Twitch Clone</p>
      <Button
        size='lg'
        variant='outline'
        style={{ width: 200 }}
      >
        Click me!
      </Button>
    </div>
  );
}
