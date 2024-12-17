<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from '@/services/QuizApiService';

const registeredScores = ref([]);
onMounted(async () => {
  console.log('Home page mounted');
  quizApiService();
});
</script>
<template>
  <h1>Home page</h1>
</template>
