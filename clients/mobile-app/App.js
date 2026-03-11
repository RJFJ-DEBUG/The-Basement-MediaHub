import React, { useEffect, useState } from "react";
import { View, Text, FlatList, TouchableOpacity, Linking, TextInput, Button, StyleSheet, ScrollView } from "react-native";

const API = "http://localhost:5000";

export default function App() {
  const [sources, setSources] = useState([]);
  const [form, setForm] = useState({ id: "", title: "", type: "video", url: "", thumbnail: "", description: "", tags: "" });

  const fetchSources = async (type = "") => {
    const url = type ? `${API}/api/sources?type=${type}` : `${API}/api/sources`;
    const res = await fetch(url);
    const data = await res.json();
    setSources(data.sources);
  };

  const addSource = async () => {
    const body = { ...form, tags: form.tags.split(",").map(t => t.trim()) };
    await fetch(`${API}/api/sources`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
    fetchSources();
  };

  useEffect(() => { fetchSources(); }, []);

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>📱 The Basement MediaHub</Text>
      <View style={styles.filters}>
        {["", "video", "audio", "image"].map(t => (
          <TouchableOpacity key={t} onPress={() => fetchSources(t)} style={styles.btn}>
            <Text style={styles.btnText}>{t || "All"}</Text>
          </TouchableOpacity>
        ))}
      </View>
      <FlatList data={sources} keyExtractor={i => i.id} renderItem={({ item }) => (
        <TouchableOpacity onPress={() => Linking.openURL(item.url)} style={styles.card}>
          <Text style={styles.cardTitle}>{item.title}</Text>
          <Text style={styles.cardType}>{item.type}</Text>
          <Text style={styles.cardDesc}>{item.description}</Text>
        </TouchableOpacity>
      )} />
      <Text style={styles.subTitle}>➕ Add Source</Text>
      {["id","title","type","url","thumbnail","description","tags"].map(field => (
        <TextInput key={field} placeholder={field} placeholderTextColor="#888" style={styles.input}
          value={form[field]} onChangeText={v => setForm(p => ({ ...p, [field]: v }))} />
      ))}
      <Button title="Add Source" onPress={addSource} color="#e50914"/>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#111", padding: 16 },
  title: { color: "#e50914", fontSize: 22, fontWeight: "bold", marginBottom: 12 },
  subTitle: { color: "#fff", fontSize: 18, marginTop: 20, marginBottom: 8 },
  filters: { flexDirection: "row", flexWrap: "wrap", marginBottom: 12 },
  btn: { backgroundColor: "#222", padding: 8, margin: 4, borderRadius: 6 },
  btnText: { color: "#fff" },
  card: { backgroundColor: "#1e1e1e", padding: 12, marginBottom: 8, borderRadius: 8 },
  cardTitle: { color: "#fff", fontSize: 16, fontWeight: "bold" },
  cardType: { color: "#e50914", fontSize: 12 },
  cardDesc: { color: "#aaa", fontSize: 13 },
  input: { backgroundColor: "#333", color: "#fff", padding: 8, marginBottom: 6, borderRadius: 6 }
});
