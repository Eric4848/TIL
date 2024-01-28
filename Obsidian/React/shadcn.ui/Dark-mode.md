## 1. next-themes 설치
```cmd
npm install next-themes
```

## 2. theme-provider.tsx파일 생성
1. components폴더에 theme-provider.tsx파일 생성
2. 내용 복사 후 붙여넣기
```tsx
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"
import { type ThemeProviderProps } from "next-themes/dist/types"

export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}

```

## 3. ThemeProvider import
```tsx
import { ThemeProvider } from "@/components/theme-provider";
```

## 4. children 감싸기
```tsx
<ThemeProvider>
  {children}
</ThemeProvider>
```

## 5. 인자 넣어주기
```tsx
<ThemeProvider
  attribute='class'
  forcedTheme='dark'
  storageKey='gamehub-theme'
>
  {children}
</ThemeProvider>
```