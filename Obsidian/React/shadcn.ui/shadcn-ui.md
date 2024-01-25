
## 1. Install
 - shadcn-ui를 사용하기 위해
```console
npx shadcn-ui@latest init
```

## 2. Button
- button component 사용하기 위해
```console
npx shadcn-ui@latest add button
```

```jsx
import {Button } from "@/components/ui/button"

export default function Test() {
	return (
	<div>
		<Button>
			Button name
		</Button>
	</div>
	)
}
```

- import 한 component들은 components/ui폴더에 저장
- 해당 파일의 variants를 수정하여 인자별 style 설정 가